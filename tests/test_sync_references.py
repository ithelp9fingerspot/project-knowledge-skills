import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "scripts" / "sync-references.py"

SKILL_DIRECTORIES = (
    "skills/auditing-project-knowledge",
    "skills/documenting-existing-projects",
    "skills/initializing-project-knowledge",
    "skills/working-with-project-specs",
    "skills/structuring-project-documentation",
)
SYNC_FILES = (
    (Path("shared/project-knowledge-standard.md"), Path("references/project-knowledge-standard.md")),
    (Path("shared/project-knowledge-authoring.md"), Path("references/project-knowledge-authoring.md")),
)


class TestSyncReferences(unittest.TestCase):
    def setUp(self):
        if not SCRIPT_PATH.exists():
            self.fail(f"scripts/sync-references.py does not exist: {SCRIPT_PATH}")
        spec = importlib.util.spec_from_file_location("sync_references", SCRIPT_PATH)
        if spec is None or spec.loader is None:
            self.fail(f"Could not load spec for {SCRIPT_PATH}")
        self.sync_module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(self.sync_module)
        except Exception as e:
            self.fail(f"Failed to execute {SCRIPT_PATH}: {e}")
        self.sync_references = getattr(self.sync_module, "sync_references", None)
        self.main = getattr(self.sync_module, "main", None)
        if self.sync_references is None or self.main is None:
            self.fail("sync_references or main not defined in scripts/sync-references.py")

    def _create_repo_structure(
        self,
        base_dir: Path,
        canonical_content: str = "# Canonical Standard\n",
        destinations_content: dict[str, str | None] | None = None,
    ) -> Path:
        """Helper to create a temporary repository tree.

        destinations_content maps skill name -> content string (or None to omit file).
        If destinations_content is None, every destination matches canonical_content.
        """
        canonical_file = base_dir / SYNC_FILES[0][0]
        canonical_file.parent.mkdir(parents=True, exist_ok=True)
        canonical_file.write_text(canonical_content, encoding="utf-8")
        (base_dir / SYNC_FILES[1][0]).write_bytes(b"# Authoring Guide\n")

        for skill in SKILL_DIRECTORIES:
            ref_dir = base_dir / skill / "references"
            ref_dir.mkdir(parents=True, exist_ok=True)
            (ref_dir / SYNC_FILES[1][1].name).write_bytes(b"# Authoring Guide\n")
            content = canonical_content if destinations_content is None else destinations_content.get(skill)
            if content is not None:
                (ref_dir / SYNC_FILES[0][1].name).write_text(content, encoding="utf-8")
        return base_dir

    def test_check_mode_reports_drift_without_mutation(self):
        with tempfile.TemporaryDirectory() as td:
            repo_dir = Path(td)
            canonical_text = "# Canonical v1\n"
            drifted_text = "# Drifted v0\n"

            # Two skills drifted, one missing, all others identical.
            destinations = {
                **{skill: canonical_text for skill in SKILL_DIRECTORIES},
                SKILL_DIRECTORIES[0]: drifted_text,
                SKILL_DIRECTORIES[1]: drifted_text,
                SKILL_DIRECTORIES[3]: None,  # Missing
            }
            self._create_repo_structure(
                repo_dir, canonical_content=canonical_text, destinations_content=destinations
            )

            file0 = repo_dir / SKILL_DIRECTORIES[0] / SYNC_FILES[0][1]
            file1 = repo_dir / SKILL_DIRECTORIES[1] / SYNC_FILES[0][1]
            file2 = repo_dir / SKILL_DIRECTORIES[2] / SYNC_FILES[0][1]
            file3 = repo_dir / SKILL_DIRECTORIES[3] / SYNC_FILES[0][1]

            mtime0 = file0.stat().st_mtime_ns
            mtime1 = file1.stat().st_mtime_ns
            mtime2 = file2.stat().st_mtime_ns

            drifted = self.sync_references(repo_dir, check=True)

            # Drifted should contain file0, file1, file3 (the missing one)
            expected_drift = {file0, file1, file3}
            self.assertEqual(set(drifted), expected_drift)

            # Verify no mutation occurred
            self.assertEqual(file0.read_text(encoding="utf-8"), drifted_text)
            self.assertEqual(file1.read_text(encoding="utf-8"), drifted_text)
            self.assertEqual(file2.read_text(encoding="utf-8"), canonical_text)
            self.assertFalse(file3.exists())

            self.assertEqual(file0.stat().st_mtime_ns, mtime0)
            self.assertEqual(file1.stat().st_mtime_ns, mtime1)
            self.assertEqual(file2.stat().st_mtime_ns, mtime2)

    def test_check_mode_parity_returns_empty(self):
        with tempfile.TemporaryDirectory() as td:
            repo_dir = Path(td)
            self._create_repo_structure(repo_dir)

            drifted = self.sync_references(repo_dir, check=True)
            self.assertEqual(drifted, [])

    def test_write_mode_repairs_all_destinations(self):
        with tempfile.TemporaryDirectory() as td:
            repo_dir = Path(td)
            canonical_text = "# Authoritative Standard Content\n"

            # Every destination needs repair.
            destinations = {
                SKILL_DIRECTORIES[0]: "# Old content\n",
                SKILL_DIRECTORIES[1]: "# Drift content\n",
                SKILL_DIRECTORIES[2]: None,
                SKILL_DIRECTORIES[3]: None,
            }
            self._create_repo_structure(
                repo_dir, canonical_content=canonical_text, destinations_content=destinations
            )

            drifted_repaired = self.sync_references(repo_dir, check=False)

            expected_paths = {
                repo_dir / s / SYNC_FILES[0][1] for s in SKILL_DIRECTORIES
            }
            self.assertEqual(len(drifted_repaired), len(expected_paths))
            self.assertEqual(set(drifted_repaired), expected_paths)

            # Verify every destination now matches canonical exactly
            for skill in SKILL_DIRECTORIES:
                dest = repo_dir / skill / SYNC_FILES[0][1]
                self.assertTrue(dest.exists(), f"Destination {dest} should exist")
                self.assertEqual(dest.read_text(encoding="utf-8"), canonical_text)

            # Subsequent check mode should find zero drift
            subsequent_drift = self.sync_references(repo_dir, check=True)
            self.assertEqual(subsequent_drift, [])

    def test_unrelated_files_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            repo_dir = Path(td)
            self._create_repo_structure(repo_dir)

            # Add unrelated files
            extra_file1 = repo_dir / SKILL_DIRECTORIES[0] / "references" / "extra-notes.md"
            extra_file1.write_text("# Extra Notes\nUnique content.\n", encoding="utf-8")

            extra_file2 = repo_dir / SKILL_DIRECTORIES[1] / "SKILL.md"
            extra_file2.write_text("# Skill Instructions\nDo not touch.\n", encoding="utf-8")

            extra_file3 = repo_dir / "shared" / "unrelated-standard.md"
            extra_file3.write_text("# Another standard\n", encoding="utf-8")

            # Introduce drift into one skill reference
            drift_target = repo_dir / SKILL_DIRECTORIES[2] / SYNC_FILES[0][1]
            drift_target.write_text("# Drifted\n", encoding="utf-8")

            repaired = self.sync_references(repo_dir, check=False)
            self.assertEqual(repaired, [drift_target])

            # Verify unrelated files are completely preserved
            self.assertTrue(extra_file1.exists())
            self.assertEqual(
                extra_file1.read_text(encoding="utf-8"),
                "# Extra Notes\nUnique content.\n",
            )

            self.assertTrue(extra_file2.exists())
            self.assertEqual(
                extra_file2.read_text(encoding="utf-8"),
                "# Skill Instructions\nDo not touch.\n",
            )

            self.assertTrue(extra_file3.exists())
            self.assertEqual(
                extra_file3.read_text(encoding="utf-8"),
                "# Another standard\n",
            )

    def test_missing_canonical_fails_without_writes(self):
        with tempfile.TemporaryDirectory() as td:
            repo_dir = Path(td)

            # Create skill reference directories with some drifted content
            dest0 = repo_dir / SKILL_DIRECTORIES[0] / SYNC_FILES[0][1]
            dest0.parent.mkdir(parents=True, exist_ok=True)
            dest0.write_text("# Existing before canonical error\n", encoding="utf-8")
            mtime0 = dest0.stat().st_mtime_ns

            dest1 = repo_dir / SKILL_DIRECTORIES[1] / SYNC_FILES[0][1]
            # dest1 does not exist

            # Ensure shared/ canonical file does NOT exist
            canonical_file = repo_dir / SYNC_FILES[0][0]
            self.assertFalse(canonical_file.exists())

            # Check mode should raise FileNotFoundError
            with self.assertRaises(FileNotFoundError):
                self.sync_references(repo_dir, check=True)

            # Write mode should raise FileNotFoundError with NO writes
            with self.assertRaises(FileNotFoundError):
                self.sync_references(repo_dir, check=False)

            # Confirm dest0 is untouched and dest1 was not created
            self.assertEqual(
                dest0.read_text(encoding="utf-8"),
                "# Existing before canonical error\n",
            )
            self.assertEqual(dest0.stat().st_mtime_ns, mtime0)
            self.assertFalse(dest1.exists())

            # main() in check and write modes should also exit non-zero without writing
            fake_script = repo_dir / "scripts" / "sync-references.py"
            fake_script.parent.mkdir(parents=True, exist_ok=True)
            fake_script.write_bytes(SCRIPT_PATH.read_bytes())

            cli_check = subprocess.run(
                [sys.executable, str(fake_script), "--check"],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(cli_check.returncode, 0)
            self.assertFalse(dest1.exists())

            cli_write = subprocess.run(
                [sys.executable, str(fake_script)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(cli_write.returncode, 0)
            self.assertFalse(dest1.exists())

    def test_invocation_from_another_working_directory(self):
        with tempfile.TemporaryDirectory() as td1, tempfile.TemporaryDirectory() as td2:
            fake_repo = Path(td1)
            other_cwd = Path(td2)

            # Set up a complete repo inside fake_repo
            self._create_repo_structure(fake_repo)

            # Copy sync-references.py to fake_repo/scripts/sync-references.py
            fake_script_dir = fake_repo / "scripts"
            fake_script_dir.mkdir(parents=True, exist_ok=True)
            fake_script = fake_script_dir / "sync-references.py"
            fake_script.write_bytes(SCRIPT_PATH.read_bytes())

            # Run from other_cwd
            result = subprocess.run(
                [sys.executable, str(fake_script), "--check"],
                cwd=str(other_cwd),
                capture_output=True,
                text=True,
            )
            self.assertEqual(
                result.returncode,
                0,
                f"Expected exit 0 from external working directory, got {result.returncode}. Stderr: {result.stderr}",
            )

    def test_main_cli_modes_and_exit_codes(self):
        with tempfile.TemporaryDirectory() as td1, tempfile.TemporaryDirectory() as td2:
            fake_repo = Path(td1)
            other_cwd = Path(td2)
            canonical_text = "# Test CLI\n"

            # Create drifted destination
            destinations = {
                **{skill: canonical_text for skill in SKILL_DIRECTORIES},
                SKILL_DIRECTORIES[0]: "# Drifted\n",
                SKILL_DIRECTORIES[1]: canonical_text,
                SKILL_DIRECTORIES[2]: canonical_text,
                SKILL_DIRECTORIES[3]: canonical_text,
            }
            self._create_repo_structure(
                fake_repo, canonical_content=canonical_text, destinations_content=destinations
            )

            fake_script = fake_repo / "scripts" / "sync-references.py"
            fake_script.parent.mkdir(parents=True, exist_ok=True)
            fake_script.write_bytes(SCRIPT_PATH.read_bytes())

            drift_file = fake_repo / SKILL_DIRECTORIES[0] / SYNC_FILES[0][1]

            # 1. --check exits 1 on drift, no mutation
            check_result = subprocess.run(
                [sys.executable, str(fake_script), "--check"],
                cwd=str(other_cwd),
                capture_output=True,
                text=True,
            )
            self.assertEqual(check_result.returncode, 1)
            self.assertEqual(drift_file.read_text(encoding="utf-8"), "# Drifted\n")

            # 2. default write mode exits 0 and repairs drift
            write_result = subprocess.run(
                [sys.executable, str(fake_script)],
                cwd=str(other_cwd),
                capture_output=True,
                text=True,
            )
            self.assertEqual(write_result.returncode, 0)
            self.assertEqual(drift_file.read_text(encoding="utf-8"), canonical_text)

            # 3. subsequent --check exits 0 on parity
            subsequent_check = subprocess.run(
                [sys.executable, str(fake_script), "--check"],
                cwd=str(other_cwd),
                capture_output=True,
                text=True,
            )
            self.assertEqual(subsequent_check.returncode, 0)

    def _snapshot(self, root):
        return {
            str(path.relative_to(root)): (path.read_bytes(), path.stat().st_mtime_ns)
            for path in root.rglob("*") if path.is_file()
        }

    def test_mixed_reference_drift_is_reported_without_any_mutation(self):
        with tempfile.TemporaryDirectory() as td:
            root = self._create_repo_structure(Path(td))
            stale = root / SKILL_DIRECTORIES[0] / SYNC_FILES[0][1]
            missing = root / SKILL_DIRECTORIES[2] / SYNC_FILES[1][1]
            stale.write_bytes(b"stale standard")
            missing.unlink()
            before = self._snapshot(root)
            self.assertEqual(set(self.sync_references(root, check=True)), {stale, missing})
            self.assertEqual(self._snapshot(root), before)

    def test_write_repairs_both_reference_types_and_preserves_unrelated_files(self):
        with tempfile.TemporaryDirectory() as td:
            root = self._create_repo_structure(Path(td))
            unrelated = root / SKILL_DIRECTORIES[0] / "references/notes.md"
            unrelated.write_bytes(b"independent notes\x00")
            expected = set()
            for skill in SKILL_DIRECTORIES:
                for _, target in SYNC_FILES:
                    dest = root / skill / target
                    dest.unlink()
                    expected.add(dest)
            self.assertEqual(set(self.sync_references(root, check=False)), expected)
            for skill in SKILL_DIRECTORIES:
                for source, target in SYNC_FILES:
                    self.assertEqual((root / skill / target).read_bytes(), (root / source).read_bytes())
            self.assertEqual(unrelated.read_bytes(), b"independent notes\x00")
            self.assertEqual(self.sync_references(root, check=True), [])

    def test_either_missing_source_aborts_before_all_writes(self):
        for source, _ in SYNC_FILES:
            for check in (True, False):
                with self.subTest(source=source, check=check), tempfile.TemporaryDirectory() as td:
                    root = self._create_repo_structure(Path(td))
                    stale = root / SKILL_DIRECTORIES[0] / SYNC_FILES[0][1]
                    stale.write_bytes(b"must survive missing later source")
                    (root / source).unlink()
                    before = self._snapshot(root)
                    with self.assertRaises(FileNotFoundError):
                        self.sync_references(root, check=check)
                    self.assertEqual(self._snapshot(root), before)

    def test_authoring_cli_drift_repair_from_external_directory(self):
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as cwd:
            root = self._create_repo_structure(Path(td))
            script = root / "scripts/sync-references.py"
            script.parent.mkdir()
            script.write_bytes(SCRIPT_PATH.read_bytes())
            target = root / SKILL_DIRECTORIES[1] / SYNC_FILES[1][1]
            target.write_bytes(b"old authoring")
            before = self._snapshot(root)
            command = [sys.executable, str(script)]
            result = subprocess.run(command + ["--check"], cwd=cwd, capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(self._snapshot(root), before)
            result = subprocess.run(command, cwd=cwd, capture_output=True)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(target.read_bytes(), b"# Authoring Guide\n")
            result = subprocess.run(command + ["--check"], cwd=cwd, capture_output=True)
            self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
