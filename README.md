# Portable Project Knowledge Skills

Portable, self-contained skills for AI coding agents to establish, navigate, evolve, and audit repository knowledge.

The primary objective is preventing silent divergence from intended business behavior and coding standards. The skills enforce strict confirmation boundaries: discrepancies between documented specifications, observed code behavior, and requested behavior require explicit developer decisions rather than automatic resolution.

All skill instructions and generated documentation are written in English.

---

## Skills and Their Triggers

| Skill Directory | Trigger / Lifecycle Phase | Key Responsibility |
|---|---|---|
| `structuring-project-documentation` | **Documentation Framework**:<br>When creating format-only outlines or reorganizing selected existing docs without implementation discovery. | Uses shared recipes, bounded source reading, and create-missing defaults; preserves legacy files and distinguishes reused claims from verified knowledge. |
| `documenting-existing-projects` | **Existing Codebase Onboarding**:<br>When introducing structured knowledge into an existing, already-implemented project. | Discovers code, schemas, and tests; asks independent legacy choices; documents grounded feature specs and standards; expresses observed code behavior in prose and records behavioral unknowns without administrative lifecycle labels. |
| `initializing-project-knowledge` | **Greenfield Project Initiation**:<br>When establishing documentation for a new, unimplemented project from agreed requirements before code or schemas exist. | Gathers purpose, scope, stack, and feature requirements; avoids premature application scaffolding or fabricated schemas; generates documentation without administrative sign-off, recording behavioral unknowns explicitly. |
| `working-with-project-specs` | **Feature Evolution & Daily Coding**:<br>When implementing, modifying, refactoring, or extending features in a project governed by project knowledge specs. | Locates specs before code changes; halts on conflicts between requested changes and documented specs; enforces spec-first updates after explicit developer authorization. |
| `auditing-project-knowledge` | **Integrity & Alignment Verification**:<br>When assessing repository knowledge health, link integrity, spec-to-code alignment, and standards adherence. | Enforces strict read-only operation (zero byte mutations, zero unrequested audit artifacts); categorizes findings into structural errors, divergence, and semantic conflicts; routes fixes without automatic rewrites. |

---

## Independent Legacy Choices

When generating documentation for an existing project (`documenting-existing-projects`), the agent must ask two independent questions upfront before reading legacy documentation prose for business meaning or writing any files:

1. **Source Choice**: May existing legacy documentation be used as an additional reference source alongside code and database schemas?
   - If **No**: Legacy documentation cannot be cited as authority for business rules. Code, migrations, and tests serve as the sole evidence base. If files must be read for preservation under merge, explicit developer permission is required.
   - If **Yes**: Legacy documentation may be used as supplementary evidence, but discrepancies between legacy prose and code must be presented to the developer rather than silently blessed.
2. **Write-Mode Choice**: Should generated documentation merge with existing documentation or replace it?
   - If **Merge**: Existing relevant documentation is preserved, duplicates are resolved deliberately, and conflicting content is flagged for developer decision.
   - If **Replace**: Replacement is strictly scoped to disclosed paths. Non-standard, compliance, or unique documentation is preserved unless explicit developer permission is given to remove or relocate it.

*Note*: If explicit answers have already been provided for the current run, the agent does not ask again.

For lightweight structuring, use the [bounded source-depth and write contract](shared/project-knowledge-standard.md#documentation-structuring) instead of implementation discovery. Outline-only is the default; selected-content reuse requires reading the selected passages, not the entire documentation tree.

---

## Example Invocations

### Documentation Format Only or Selected-Content Reuse
```text
"Use structuring-project-documentation to create the standard documentation framework.
Use only docs/legacy.md#local-setup as content for docs/development.md; keep other
sections as filling prompts. Preserve existing files and do not inspect application code."
```
The result is an explicitly incomplete framework, not approved feature behavior or code/doc alignment evidence. Without a selected source, the skill can create outlines from the shared formats alone.

### 1. Documenting an Existing Project
```text
"Inspect this repository and generate complete project knowledge documentation following
our project knowledge standard. Do not treat old docs as authority until I specify,
and ask me how to handle existing documentation before writing files."
```
*Expected Agent Behavior*: Scans filenames without reading prose for business rules; asks the two legacy choices in a single batched prompt; explores schemas, migrations, code, and tests; generates specifications with observed implementation described in prose and unknowns placed in Open Questions without administrative status labels; halts on conflicts or before coding ambiguous behavior.

### 2. Initializing a Greenfield Project
```text
"Initialize project knowledge for a new appointment booking platform. Stack is Go with
PostgreSQL. We have not finalized the physical database schema or payment provider.
Prepare the initial knowledge base and booking spec."
```
*Expected Agent Behavior*: Creates `README.md`, `AGENTS.md`, `CLAUDE.md`, `docs/project.md`, `docs/architecture.md`, and initial specs in `docs/specs/` with behavioral unknowns recorded in Open Questions; sets `Implementation: Not yet available` and `Tests: Not yet available`; defers `docs/data-model.md` until storage schema is concrete; does not run framework scaffolding commands (`go mod init`, etc.) or demand administrative sign-off.

### 3. Working with Project Specifications
```text
"Update billing logic to allow customers without active base subscriptions to purchase
addons directly. Update the code and tests right away."
```
*Expected Agent Behavior*: Locates `docs/specs/billing/addon-purchase.md` and checks rule `BR-ADDON-001`; detects that the request conflicts with a documented rule; stops before modifying any files; presents the conflict neutrally with rule and file references; requests explicit developer authorization before updating spec and implementing code.

### 4. Auditing Project Knowledge
```text
"Audit all project knowledge documentation in this repository. Verify structural links,
spec-to-code alignment, and standards compliance. Report any issues found."
```
*Expected Agent Behavior*: Performs read-only scans; checks link integrity, implementation mappings, and schema parity; writes zero files to the target repository; reports findings grouped by severity and category with clear workflow routing.

---

## Target Repository Documentation Contract

Standard layout produced in target repositories:

```text
README.md                     # Concise introduction and routing
AGENTS.md                     # Shared agent instruction entrypoint and map
CLAUDE.md                     # Single-line Claude import of AGENTS.md
docs/
  README.md                   # Task-oriented documentation navigation
  project.md                  # Purpose, users, glossary, stack manifests
  architecture.md             # Module boundaries, dependencies, design rationale
  data-model.md               # App-wide ERD and entities (when persistent data exists)
  development.md              # Prerequisites, setup, commands, troubleshooting
  standards/
    coding.md                 # Language/framework conventions grounded in linter/code
    testing.md                # Test layers, fixtures, execution commands
    ui.md                     # Component contracts, tokens, accessibility (when UI exists)
  workflows/
    spec-changes.md           # Lifecycle for proposing, approving, and verifying specs
  specs/
    README.md                 # Specification index and lifecycle overview
    <domain>/
      <feature>.md            # Grounded feature specs with stable rule IDs (BR-[DOMAIN]-[001])
```

Optional `docs/decisions/` is created only when a durable technical architectural decision warrants an Architecture Decision Record (ADR). Content-authoring workflows create grounded documents; explicitly requested structuring creates labelled outlines instead. Keep recognized entrypoints uppercase and other documentation lowercase kebab-case. Substantial contextual guides such as `docs/standards/typescript.md` or `api.md` are created only when needed, with one content owner and task-conditioned links; their names do not cause automatic loading.

---

## Architecture and Packaging Design

### Shared Standard as Authoring Authority
The single authoritative source for documentation rules, feature spec formats, approval boundaries, and evidence hierarchies is:
```text
shared/project-knowledge-standard.md
```

### Self-Contained Standalone Packages
To ensure that installing a single skill does not fail due to missing sibling directories or authoring files, each skill directory is packaged as a completely independent distribution:
```text
skills/
  documenting-existing-projects/
    SKILL.md
    references/project-knowledge-standard.md
  initializing-project-knowledge/
    SKILL.md
    references/project-knowledge-standard.md
  working-with-project-specs/
    SKILL.md
    references/project-knowledge-standard.md
  auditing-project-knowledge/
    SKILL.md
    references/project-knowledge-standard.md
  structuring-project-documentation/
    SKILL.md
    references/project-knowledge-standard.md
```

Each `SKILL.md` accesses its bundled standard via the relative link `references/project-knowledge-standard.md`. There are no mandatory sibling links or runtime package dependencies.

Only `skills/` contains installable packages. Root-level `shared/`, `scripts/`, `tests/`, and `docs/` hold the authoring standard, maintenance tooling, verification scenarios, and design history respectively. Keep each skill's folder name equal to its frontmatter `name`.

### Thin `CLAUDE.md` Routing
Generated `CLAUDE.md` contains only the import prescribed by the [canonical entrypoint contract](shared/project-knowledge-standard.md#root-entrypoints). The [authoring recipe](shared/project-knowledge-authoring.md#claudemd) shows its complete contents. `AGENTS.md` remains the shared instruction owner. This one Claude-specific eager import differs from ordinary task-conditioned Markdown pointers; splitting a manual into eager imports does not reduce loaded context.

### Safe Merges and Unfinished Documents
Authorized merges preserve unique meaning while applying the current document recipes, not legacy layout. Generated and merged `AGENTS.md` files include task routing, target 60–100 physical lines, and never exceed 150; task-specific detail moves behind scoped links without dropping instructions. Shorter sufficient files need no padding. This line budget is project policy, not a universal agent limit.

Scaffolds and partially filled documents carry visible incomplete-content and action-required notices, concrete section-level filling instructions, and incomplete labels in inbound navigation. Templates and examples are not project requirements or executable procedures. See the [structuring safeguards](shared/project-knowledge-standard.md#documentation-structuring) and [AGENTS recipe](shared/project-knowledge-authoring.md#agentsmd).

---

## Installation and Host-Loading Limitations

These skills are plain Markdown packages containing instructions and reference files. They do not require custom package managers, MCP servers, slash commands, or Claude-specific hooks.

### Install with the skills CLI

The [skills CLI](https://github.com/vercel-labs/skills) discovers packages under `skills/`. Run it through `npx` with Node.js and npm available; no npm package, plugin manifest, or registry publishing step is needed for this repository.

After hosting this repository on GitHub, replace `<owner>/<repo>` below with its actual repository identifier:

```bash
# List available skills without installing
npx skills add <owner>/<repo> --list

# Install one skill into the current project (choose the target agent interactively)
npx skills add <owner>/<repo> --skill documenting-existing-projects

# Install all skills into the current project, targeting Claude Code
npx skills add <owner>/<repo> --skill '*' --agent claude-code
```

Do not use `--all` merely to select all skills: it also selects all agents and skips confirmation. Add `--global` only when installation into the user's skill directories is intended.

For local discovery before publishing, run from this repository's root:

```bash
npx skills add . --list
```

The list operation does not install skills. `npx` may download the CLI into npm's cache. The following disables installation telemetry for local verification:

```bash
DISABLE_TELEMETRY=1 npx skills add . --list
```

For manual installation, copy the entire `skills/<skill-name>/` directory, including `references/`, into the target host's documented skill directory. Host-specific locations vary; arbitrary repository folders are not guaranteed to be discovered.

### Availability on skills.sh

GitHub hosting makes the repository usable as a CLI source. [skills.sh's FAQ](https://skills.sh/docs/faq) states that leaderboard entries are recorded automatically through installation telemetry; a local discovery check does not publish a listing or prove leaderboard inclusion.

### Runtime Limitations & Evidence Scope
- **Host Runtime Variance**: Actual skill discovery and prompt injection depend entirely on the host environment. The repository guarantees portable Markdown contracts and bundled reference links; it does not claim universal automatic skill discovery across all third-party agents.
- **Observed Verification**: Verification evidence in this repository was obtained through explicit tool executions and simulated developer turns using host `sdd-implementer` coding agents on Linux x64. Evidence does not claim untested host environments or unverified automatic invocation.
- **Installation Scope**: The CLI writes skill files and host-specific links in the selected project or user skill directories. These instructions default to project scope; no global installation, host configuration changes, or remote publication are part of repository verification.

---

## Maintenance and Testing Commands

All scripts and tests use the Python 3 standard library with zero external package dependencies.

Canonical documentation contracts live in `shared/project-knowledge-standard.md`; detailed per-file outlines and writing recipes live in `shared/project-knowledge-authoring.md`. Edit those sources only. Both files are bundled under each skill's `references/` directory so a standalone installation needs no sibling skill or source-repository access. Recipes standardize English headings and order, while contents follow the target project's evidence and decisions. `AGENTS.md` routes tasks; `docs/architecture.md#repository-map` owns project structure; development owns invocation procedures.

### 1. Synchronizing Packaged References
To propagate edits from both canonical references in `shared/` to every skill package:
```bash
python3 scripts/sync-references.py
```

### 2. Checking Reference Parity
To verify that all packaged references match their canonical sources without modifying files (exits `0` on parity, `1` on drift or missing source):
```bash
python3 scripts/sync-references.py --check
```

### 3. Running Unit Tests
To execute the packaging and synchronization test suite:
```bash
python3 -m unittest discover -s tests -v
```

---

## Behavioral Scenario Execution

Behavioral scenarios and evaluation rubrics live in `tests/scenarios/`:
- `tests/scenarios/structuring-project-documentation.md`: Scenarios S1–S3 (format-only, selected legacy reuse, existing-file collision and preservation).
- `tests/scenarios/documenting-existing-projects.md`: Scenarios E1–E4 (legacy choices, no-source merge, narrow replace, non-English docs).
- `tests/scenarios/initializing-project-knowledge.md`: Scenarios N1–N3 (empty project decisions, UI initialization, in-scope vs future roadmap scope).
- `tests/scenarios/working-with-project-specs.md`: Scenarios W1–W3 (spec/code divergence, scope expansion stop, new feature spec creation).
- `tests/scenarios/auditing-project-knowledge.md`: Scenarios A1–A3 (read-only invariant, semantic conflicts, unimplemented planned specs without lifecycle metadata).
- `tests/scenarios/standalone-installation.md`: Scenarios P1–P2 (standalone skill portability, thin CLAUDE routing and conflict stop).

### Execution Protocol
1. **Disposable Fixtures**: Scenarios must always run against throwaway directories in temporary storage (e.g. `/tmp/test-fixture-...`), never against production or real application projects.
2. **Fresh Agent Sessions**: Run baseline (unassisted) and verification (skill-assisted) sessions in clean contexts to observe comparative behavior.
3. **Observation & Logging**: Record verbatim tool calls and conversation turns. Inspect generated files for structure, grounded precision, and absence of fabricated decisions.
4. **Source of Truth**: Observed agent behavior and fixture diff inspections constitute the sole evidence of compliance. Markdown rules alone do not prove behavioral safety.
5. **Authoring Coverage**: Exercise ordered formats, grounded unknowns, conditional UI/storage omissions, architecture-owned repository maps, development-owned command procedures, and cross-domain spec selection. Copy the complete two-reference package for isolated runs; generated project links must remain self-contained. Audit scenarios compare target bytes before and after and report defects without repair.

---

## Research Basis and Stated Limits

The principles guiding this repository's design draw upon established engineering practices for AI coding agents and team knowledge systems:

1. **Google Software Engineering at Google (Chapter 10: Documentation)**:
   - Emphasizes clear document boundaries, peer review in change history, and traceable documentation maintenance.
   - Reference: https://abseil.io/resources/swe-book/html/ch10.html
2. **OpenAI Harness Engineering**:
   - Describes concise `AGENTS.md` entrypoints as maps rather than exhaustive manuals, organizing structured repository knowledge for autonomous coding agents.
   - Reference: https://openai.com/index/harness-engineering/
3. **Anthropic Claude Code Best Practices**:
   - Recommends concise shared instructions, modular context loaded on demand, and avoiding instruction duplication across prompt files.
   - Reference: https://code.claude.com/docs/en/best-practices
4. **Spotify Engineering (Code with Claude)**:
   - Highlights shared context architectures enabling human developers and AI agents to operate against the same catalog and standards.
   - Reference: https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint

### Limits of Research Application
These references provide foundational principles for concise instruction routing, structured context, and human approval boundaries. They do not prescribe the exact naming conventions, skill decomposition, per-feature ERD requirement, or standalone packaging structure implemented here. Those choices are project-specific design adaptations.
