# Project Knowledge Authoring Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Standardize project-document formats and provide detailed per-file writing recipes while grounding every document's content in its project.

**Architecture:** Retain the normative standard and add one on-demand authoring reference. Extend existing distribution to bundle both references with four standalone skills; update writing/audit routes and evaluate resulting documentation in disposable fixtures.

**Tech Stack:** Markdown, Python 3 standard library, unittest, fresh agent behavioral scenarios.

**Spec:** [Project Knowledge Authoring Design](../specs/2026-10-21-project-knowledge-authoring-design.md)

**Status:** Awaiting approval together with the design. No guide or sync implementation has been made.

## Global Constraints

- Standardize document format; content always adapts to the project.
- Use scout agents for project exploration.
- Keep `AGENTS.md` authoritative across general coding agents; always generate a thin `CLAUDE.md` entrypoint linking to it.
- Generated prose is English; preserve exact project identifiers and existing evidence, approval, legacy, and portability policies.
- Canonical reference sources are `shared/project-knowledge-standard.md` and `shared/project-knowledge-authoring.md`; packaged copies are generated, not hand-edited.
- Preserve `sync_references(root: Path, check: bool) -> list[Path]` and existing CLI flags, output conventions, and exit codes.
- No Fingerspot backend changes, empty scaffolds, application implementation, or new skill/runtime dependency.
- Feature-spec structure stays authoritative in the standard; other outlines and authoring recipes belong to the guide.

## Review Focus

1. Empty or undecided projects receive truthful unknowns, not invented modules, storage, owners, or approval: Task 3, N1.
2. Conditional UI/persistence guidance does not create irrelevant files or fabricated defaults: Task 3, N1/N2.
3. Overlapping domain terms route to every affected spec rather than an arbitrary single match: Task 3, E1 extension.
4. An isolated installation reaches both references, while generated project links remain inside that project or valid external references: Task 3, standalone extension.
5. Missing second canonical input causes failure before any destination write; drift checking remains non-mutating: Task 2, missing-input and mixed-drift tests.

## File Map and Execution

Create the authoring guide; modify the standard, `scripts/sync-references.py`, `tests/test_sync_references.py`, four consumer `SKILL.md` files, applicable scenario Markdown files, and `README.md`. Regenerate eight bundled reference files across the four package reference directories. Use existing scenario files rather than introduce another evaluation framework.

Execute inline on a new `project-knowledge-authoring` branch in this checkout after approval. Tasks share the canonical content/packaging contract and run sequentially; a final fresh whole-branch reviewer checks their seams. Scouts handle any further repository exploration. Do not add compatibility aliases for replaced internal constants; exact repository search found uses only in the sync script and its tests.

### Task 1: Define the Format Contract and Authoring Recipes

**Files:**
- Modify: `shared/project-knowledge-standard.md` — Document Responsibilities, command ownership, format/pointer and verification rules.
- Create: `shared/project-knowledge-authoring.md`.
- Modify: `tests/scenarios/initializing-project-knowledge.md` and `tests/scenarios/documenting-existing-projects.md` — authoring-specific acceptance additions.

**Interfaces:**
- Consumes: the design's ordered outlines, recipe structure, applicability rules, and existing standard's feature-spec schema.
- Produces: canonical `project-knowledge-authoring.md`, including `#agentsmd`, `#docsarchitecturemd`, and `#feature-specifications` recipe anchors; standard-to-guide and guide-to-standard links use same-directory filenames. Other recipe anchors follow descriptive filename headings and are checked before consumer references are added.

- [ ] **Step 1:** Extend N1, N2, and E1 observable assertions before writing the guide. Specify ordered headings and conditional omissions, project-specific facts, unresolved decisions, thin CLAUDE, architecture repository-map ownership, and the separation of intended behavior from implementation observations. Preserve existing scenario safeguards. These are behavioral criteria, not source-text snapshot tests.
- [ ] **Step 2:** Create the guide using all seven recipe fields from the design. Cover every standard file, feature specs by link to their authoritative schema, and conditional ADRs. Include compact illustrative task-routing and semantic repository-map examples; guide examples must not become project requirements. Mark conditional sections with plain prose `Include when: <condition>` outside destination headings. Use the exact headings/order in the design, and describe supported unknowns instead of generic filler.
- [ ] **Step 3:** Update the standard with format requirements and a conditional authoring pointer, canonical repository-map placement, and development/testing command ownership. Keep current evidence and approval rules unchanged. Do not duplicate outlines or feature templates across files. Clarify the optional ADR authoring pointer without creating an ADR directory.
- [ ] **Step 4:** Perform a recipe-to-document coverage check against the standard layout and walk the two cross-reference directions. Confirm every destination outline has conditions for any optional section and an observable completion criterion. Record exact static checks performed; agent compliance is not claimed until Task 3's scenarios run.
- [ ] **Step 5:** Commit only this task's owned paths after its checks, with message `docs: define project-specific documentation authoring formats`.

### Task 2: Distribute Both Canonical References Safely

**Files:**
- Modify: `scripts/sync-references.py:8-44`.
- Modify: `tests/test_sync_references.py` — fixtures and existing check/write/CLI tests.
- Generate: `skills/{initializing-project-knowledge,documenting-existing-projects,working-with-project-specs,auditing-project-knowledge}/references/{project-knowledge-standard.md,project-knowledge-authoring.md}`.

**Interfaces:**
- Consumes: Task 1's two canonical Markdown files.
- Produces: `SYNC_FILES: tuple[tuple[Path, Path], ...]` with the two explicit shared-to-references mappings; unchanged `sync_references(root: Path, check: bool) -> list[Path]`, `main(argv: list[str] | None = None) -> int`, CLI, and `SKILL_DIRECTORIES`.

- [ ] **Step 1:** Update fixture support and add failing behavioral tests for both reference names. Assert that mixed stale/missing destinations are returned exactly, check mode preserves full tree bytes, write mode repairs all eight declared destinations and preserves unrelated bytes, and either missing canonical file raises `FileNotFoundError` without any writes. Make a first-reference target stale when the second source is absent to expose premature writes. Retain working-directory independence and CLI exit-code coverage for drift in either reference. Assertions use expected path sets and destination bytes, not only counts or constant values.
- [ ] **Step 2:** Run `python3 -m unittest discover -s tests -p test_sync_references.py -v`; observe the added cases fail against the single-reference implementation. Retain the failure output as verification evidence.
- [ ] **Step 3:** Replace single-file internal constants with `SYNC_FILES`, migrate callers in the test fixture, and preload all canonical bytes before creating directories or writing any destination. Then compare/write declared destinations and return drift paths deterministically. Preserve existing output conventions and avoid unrelated refactors or compatibility aliases.
- [ ] **Step 4:** Run the same targeted unittest command once after the fix. Exercise the actual CLI in a disposable fixture: parity exits 0, stale authoring reference makes `--check` exit 1 with no byte changes, write mode repairs it, and a subsequent check exits 0. Invoke the CLI from a different working directory using the fixture's real script path, following the existing test fixture pattern.
- [ ] **Step 5:** Run `python3 scripts/sync-references.py` to generate all packaged references, then `python3 scripts/sync-references.py --check`. Expect parity and exit 0. Commit only this task's script, test, and generated-reference paths with message `feat: bundle documentation authoring reference in every skill`.

### Task 3: Route Consumers and Verify Agent Behavior

**Files:**
- Modify: `skills/initializing-project-knowledge/SKILL.md` — writing phase near the current standard pointer at line 149.
- Modify: `skills/documenting-existing-projects/SKILL.md` — writing phase near line 104.
- Modify: `skills/working-with-project-specs/SKILL.md` — affected-spec authoring path; shared references currently near line 198.
- Modify: `skills/auditing-project-knowledge/SKILL.md` — relevant-file format audit path; shared references currently near line 184.
- Modify: `tests/scenarios/standalone-installation.md`, `tests/scenarios/initializing-project-knowledge.md`, `tests/scenarios/documenting-existing-projects.md`, and `tests/scenarios/auditing-project-knowledge.md`.
- Modify: `README.md:208-249` and relevant overview text describing the reference bundle.

**Interfaces:**
- Consumes: Task 1 recipe anchors and Task 2 standalone two-reference packaging.
- Produces: writing/audit pointers that load only relevant recipes, updated behavioral scenarios, and maintenance documentation for both references.

- [ ] **Step 1:** Put conditional guide pointers at actual writing or auditing steps. A spec-only change routes to the feature-spec recipe; audit reads affected document recipes without gaining write authorization. Keep discovery and approval gates before authoring. Do not make all recipes compulsory at session startup or turn the generated project into a consumer of installed skill paths.
- [ ] **Step 2:** Extend standalone and audit scenarios: install one complete skill package in a disposable directory, deny sibling/source-repository access, then navigate local standard/guide links. Require the generated CLAUDE-to-AGENTS-to-architecture/spec/development routes to resolve inside the generated project. Audit must identify a format/content-ownership problem without editing files. Add an E1 follow-up after explicit legacy choices, distinguishing catalog pricing from billing configuration and checkout calculation and requiring all affected specs for a cross-domain task. Update README to explain the canonical pair, generated copies, and the existing maintenance commands.
- [ ] **Step 3:** Execute baseline and skill-assisted runs in fresh sessions with disposable fixtures, following README's scenario protocol. Run N1 (empty), N2 (UI), E1 plus cross-domain follow-up (backend), standalone isolation, and read-only format audit. Capture actual conversation/tool evidence and inspect outputs for heading order, conditional omission, grounded facts, approvals, content ownership, and valid navigation. Never run these scenarios against Fingerspot or any real application repository. Fix actual guidance defects and rerun only the affected scenario; do not weaken acceptance criteria to fit output.
- [ ] **Step 4:** Remove disposable smoke fixtures created for the implementation after capturing evidence outside the target repository. Run `python3 -m unittest discover -s tests -v` once and `python3 scripts/sync-references.py --check`. Check changed local Markdown file and section links, distinguishing illustrative destination paths from actual skill-package dependencies. Expected: all unit tests pass, sync exit 0, real local reference links resolve, and no generated project depends on skill-repository paths.
- [ ] **Step 5:** Commit only owned consumer, scenario, and README changes with message `docs: route project knowledge skills through file authoring recipes`. Request one fresh final whole-branch review covering the design, canonical guidance, all consumers, synchronization failure paths, and observed scenario evidence. Address findings and rerun the affected verification before reporting completion.

## Approval Handoff

Approve the design and this three-task plan together. Proposed execution is inline, with scouts for exploration and a fresh final reviewer, on a new `project-knowledge-authoring` branch in this checkout. The planning workspace was clean before creating these two planning documents. No implementation, application changes, or scenario execution has occurred during planning.
