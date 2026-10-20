#!/usr/bin/env python3
"""Synchronize shared project-knowledge-standard.md to standalone skill packages."""

import argparse
from pathlib import Path
import sys

SKILL_DIRECTORIES = (
    "auditing-project-knowledge",
    "documenting-existing-projects",
    "initializing-project-knowledge",
    "working-with-project-specs",
)

CANONICAL_RELPATH = Path("shared") / "project-knowledge-standard.md"
TARGET_RELPATH = Path("references") / "project-knowledge-standard.md"


def sync_references(root: Path, check: bool) -> list[Path]:
    """Check or synchronize the canonical reference across skill packages.

    Returns the list of missing or different destination paths.
    In write mode (check=False), copies canonical reference to drifted destinations.
    In check mode (check=True), performs no filesystem writes.
    Raises FileNotFoundError if the canonical source does not exist.
    """
    root = Path(root)
    canonical = root / CANONICAL_RELPATH
    if not canonical.is_file():
        raise FileNotFoundError(f"Canonical reference not found: {canonical}")

    canonical_bytes = canonical.read_bytes()
    drift: list[Path] = []

    for skill in SKILL_DIRECTORIES:
        dest = root / skill / TARGET_RELPATH
        if not dest.is_file() or dest.read_bytes() != canonical_bytes:
            drift.append(dest)

    if not check:
        for dest in drift:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(canonical_bytes)

    return drift


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint rooting at the script's repository."""
    parser = argparse.ArgumentParser(
        description="Synchronize canonical project-knowledge-standard.md to standalone skills."
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
