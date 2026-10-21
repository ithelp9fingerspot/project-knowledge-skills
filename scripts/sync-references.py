#!/usr/bin/env python3
"""Synchronize canonical project knowledge references to standalone skill packages."""

import argparse
from pathlib import Path
import sys

SKILL_DIRECTORIES = (
    "skills/auditing-project-knowledge",
    "skills/documenting-existing-projects",
    "skills/initializing-project-knowledge",
    "skills/working-with-project-specs",
    "skills/structuring-project-documentation",
)

SYNC_FILES: tuple[tuple[Path, Path], ...] = (
    (Path("shared/project-knowledge-standard.md"), Path("references/project-knowledge-standard.md")),
    (Path("shared/project-knowledge-authoring.md"), Path("references/project-knowledge-authoring.md")),
)


def sync_references(root: Path, check: bool) -> list[Path]:
    """Return drifted targets, repairing them unless check mode is requested.

    Load every canonical input before writing so a missing source never causes
    a partial update. Check mode performs no filesystem writes.
    """
    root = Path(root)
    sources = []
    for source, target in SYNC_FILES:
        canonical = root / source
        if not canonical.is_file():
            raise FileNotFoundError(f"Canonical reference not found: {canonical}")
        sources.append((target, canonical.read_bytes()))

    drift: list[Path] = []
    for target, canonical_bytes in sources:
        for skill in SKILL_DIRECTORIES:
            dest = root / skill / target
            if not dest.is_file() or dest.read_bytes() != canonical_bytes:
                drift.append(dest)
                if not check:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(canonical_bytes)
    return drift


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint rooting at the script's repository."""
    parser = argparse.ArgumentParser(
        description="Synchronize canonical project knowledge references to standalone skills."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check for reference drift without performing writes. Exits 0 on parity, 1 on drift.",
    )
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parent.parent

    try:
        drift = sync_references(repo_root, check=args.check)
    except FileNotFoundError as err:
        sys.stderr.write(f"Error: {err}\n")
        return 1

    if args.check:
        if drift:
            for path in drift:
                sys.stderr.write(f"Reference drift: {path}\n")
            return 1
        return 0

    if drift:
        for path in drift:
            sys.stdout.write(f"Synchronized {path}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
