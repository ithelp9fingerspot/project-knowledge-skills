---
name: documenting-existing-projects
description: Use when documenting an existing codebase, reverse-engineering architecture and specs, or establishing repository knowledge from existing code
---

# Documenting Existing Projects

## Overview
Establishes standardized repository documentation from an existing codebase through evidence-based inspection without silently overwriting legacy material or guessing business intent.

## When to Use
- Documenting an existing or inherited repository.
- Reverse-engineering architecture, data models, or feature specifications from code, schema, and tests.
- Establishing repository standards (`AGENTS.md`, `docs/`) for a project that lacks them.

## When NOT to Use
- Scaffolding formats or reorganizing selected existing docs without code discovery (use `structuring-project-documentation`; existing code does not change that routing).
- Creating a brand new, empty, or un-implemented project (use `initializing-project-knowledge`).
- Updating specs for day-to-day feature work or bugfixes (use `working-with-project-specs`).
- Verifying existing documentation against code in a read-only audit (use `auditing-project-knowledge`).

---

## The Two Independent Legacy Choices (Mandatory Gate)

When encountering an existing project with existing documentation, **STOP before reading legacy prose for business meaning or writing any files**.

You must obtain answers to two independent choices. If not already explicitly provided, ask both questions in a single batched prompt:

1. **Legacy Source Choice**: May existing legacy documentation be used as an additional reference source for business rules and intent alongside code and schema?
2. **Write-Mode Choice**: Should new documentation **merge** with existing documentation, or **replace** existing documentation?

```mermaid
flowchart TD
    start{"Existing docs detected?"}
    choices_known{"Both choices explicitly given?"}
    ask_choices["STOP: Ask both legacy choices<br/>Source usage and merge or replace"]
    inspect_code["Inspect code, schema, manifests"]

    start -->|Yes| choices_known
    start -->|No| inspect_code
    choices_known -->|Yes| inspect_code
    choices_known -->|No| ask_choices
    ask_choices -->|Answers received| inspect_code
```

### Enforcing the Source Choice
- **Allowed as source**: You may inspect legacy docs. Discrepancies between legacy prose and code must be presented neutrally as conflicts for developer resolution.
- **Excluded (no-source)**: Do NOT read legacy prose to infer business logic. Do NOT cite excluded legacy documents as evidence in specifications. Derive rules strictly from code, database schemas, configuration, and developer answers.

### Enforcing the Write-Mode Choice
- **Merge Mode**:
  - Preserve existing unique operational documents, runbooks, and compliance notes.
  - Normalize authorized merged destinations to the current recipes, preserving unique meaning rather than legacy layout. Apply the standard's merge rules and AGENTS recipe; account for relocated guidance and obtain scope for any additional destination before moving content.
  - If `no-source` was chosen, reading legacy files for preservation (e.g. checking whether a file has unique operational notes) **requires explicit developer permission first**, stating the preservation-only purpose.
- **Replace Mode**:
  - Replacement scope is strictly limited to disclosed standard destination paths (`README.md`, `AGENTS.md`, `CLAUDE.md`, and standard `docs/` paths) plus individually disclosed, specifically authorized nonstandard sources being replaced or relocated into the new structure (e.g. migrating `docs/overview.md` or `docs/deploy-manual.md`).
  - **NEVER perform recursive deletion** (`rm -rf docs/` or directory wipes).
  - Any undisclosed, out-of-scope, or unique document (e.g. `docs/compliance/soc2-audit-notes.md`, custom operational playbooks) must remain untouched unless specific authorization is granted.
---

## Execution Workflow

### Phase 1: Fast Inventory & Choice Verification
1. List file trees and identify existing documentation (`README.md`, `docs/`, wiki files, notes).
2. Check if the developer provided both the legacy source choice and write-mode choice.
3. If either choice is missing, ask both questions together. Do not read legacy prose for business meaning yet.

### Phase 2: Grounded Code Discovery
1. Use scoped scouts when supported by the host runtime; otherwise inspect files directly.
2. Read project manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`) to identify language, dependencies, and build commands. Do not copy dependency versions into prose documents.
3. Inspect linter/formatter configurations to establish coding standards. Never invent generic policies (e.g. PEP 8, generic style guides) from tiny code fixtures; label unconfigured patterns as proposals until approved.
4. Inspect database schemas, migrations, and ORM models to reconstruct the data model.
5. Before choosing spec files, read the [capability-boundary contract](references/project-knowledge-standard.md#capability-boundaries). Inventory every in-scope capability by tracing entrypoints, routes, service operations, schema effects, and tests; domain names are grouping labels, not completed specs. Apply the contract's grouping and coverage rules rather than using one overview or one file per endpoint.
   - Distinguish return values from side effects (e.g. returning `True` from an eligibility check is not the same as mutating state or cancelling an entity).
   - Do not strengthen terminology beyond code identifiers (e.g. `GRACE_DAYS = 7` is 7 days, NOT "calendar days" or "business days" without explicit backing).
   - Do not assert unevidenced architectural guarantees (e.g. thread-safety, atomicity) without explicit concurrency primitives.
6. Inspect automated tests to observe developer test expectations.
   - **Crucial**: Existing tests prove implementation expectations and assertions, NOT approved business intent.
   - Describe code-derived claims as observed behavior with their sources, not developer-endorsed requirements.
   - **Done:** every discovered capability has an evidence trail, a proposed spec or justified grouped stage, and enumerated main/alternate/rejection paths; untraced paths are explicit gaps, not silently excluded.
### Phase 3: Target File Mapping & Scope Disclosure
Present the planned documentation mapping to the developer before writing files:
- Files to create (e.g. `AGENTS.md`, `CLAUDE.md`, `docs/project.md`, `docs/architecture.md`, `docs/data-model.md`, `docs/specs/...`).
- Files to update or merge into (under merge mode).
- Files to replace or relocate (under replace mode: disclosed standard destination paths and individually disclosed, specifically authorized nonstandard sources).
- Files preserved untouched (undisclosed, out-of-scope, or unique operational, compliance, and legacy files).
- Capability-to-spec mapping, grouped-stage rationale, and discovery gaps; disclose coverage before treating the domain as documented.

### Phase 4: Neutral Conflict Presentation
If code, tests, legacy documentation (when allowed as source), or requirements disagree:
- **Do not guess or pick a winner.** Code being newer or tests passing does not constitute business approval.
- Present each conflict with:
  1. Documented rule or legacy statement (file and line reference).
  2. Observed code behavior and test expectations (file and line references).
  3. Risk or behavioral impact.
  4. Specific question/decision needed from the developer.

### Phase 5: Generation Boundaries
Generate the requested documents from permitted evidence without owner assignment or administrative sign-off. Record unresolved behavioral questions and source conflicts rather than silently deciding them. If replace mode was selected, obtain any still-missing authorization for the disclosed replacement mapping; explicit authorization already supplied is sufficient.

### Phase 6: Documentation Generation & Verification
1. Author documentation according to the [Project Knowledge Standard](references/project-knowledge-standard.md). At this writing phase, read only the affected file recipes in the [Authoring Guide](references/project-knowledge-authoring.md); apply their headings/order using permitted project evidence. Use [AGENTS guidance](references/project-knowledge-authoring.md#agentsmd) for task conditions and [architecture guidance](references/project-knowledge-authoring.md#docsarchitecturemd) for the single authoritative Repository Map. Preserve the earlier legacy-source and write-mode decisions.
2. **Language Invariant**: All generated documentation files must be in **English**, regardless of the user's prompt language or legacy document language.
3. **Identifier Preservation**: Preserve exact code identifiers, method names, table columns, and error strings.
4. **No Invented Failure Rules**: Do not elevate low-level language runtime type errors (e.g. `TypeError` on invalid constant types) into approved business failure rules.
5. **Open Acceptance Criteria**: Acceptance criteria must remain open checkboxes `[ ]`. NEVER mark them checked `[x]` without observed test execution.
6. **Thin CLAUDE Entrypoint**: Apply the exact [CLAUDE recipe](references/project-knowledge-authoring.md#claudemd); verify its import target exists.
7. Verify:
   - Check all relative Markdown links.
   - Check feature ERDs match the shared data model in `docs/data-model.md`.
   - Confirm observations and intended requirements remain distinguishable, with no administrative lifecycle fields.
   - Ensure no temporary discovery artifacts or `changes/` folders were created.
   - Reconcile the capability inventory with generated specs: each discovered flow and rejection branch is documented with its evidence or reported as unverified. A domain overview alone cannot satisfy capability coverage.
---

## Rationalization Table & Red Flags

| Rationalization | Reality | Correction |
|---|---|---|
| "I should read the README first to understand the project before asking questions." | Reading legacy prose before the source-choice decision biases discovery and violates developer intent. | Stop. Check file paths only. Ask both legacy choices before reading prose. |
| "User chose merge mode, so I must read all old docs to know what to merge." | In `no-source` mode, reading legacy docs without prior consent risks incorporating unapproved business claims. | Ask permission first: explain that the read is strictly for operational preservation, not business logic. |
| "User said REPLACE docs and clean everything up, so I can wipe `docs/`." | Replacing docs never authorizes blanket directory deletion or deleting undisclosed/unauthorized compliance or ops docs. | Propose a narrow file mapping of standard paths and authorized nonstandard sources to replace/relocate. Leave undisclosed unique files untouched. |
| "Code is newer and unit tests pass, so the code behavior is the approved rule." | Green tests prove code consistency, not business authorization. An implemented bug has green tests. | Present the discrepancy neutrally with evidence from both sources. Await developer decision. |
| "The user asked in another language, so I should write docs in that language." | Project knowledge documentation must be universally portable across agents and tools in English. | Conversational replies follow user language, but generated repository documents are strictly English. |
| "The feature is implemented, so its inferred rules are endorsed requirements." | Implementation demonstrates current behavior, not developer intent. | Generate sourced observations and record unresolved intent without requesting administrative sign-off. |
| "The code runs and tests pass, so I can check off acceptance criteria `[x]`." | Acceptance criteria in specs are requirements to verify, not past test execution logs. | Keep criteria as open `[ ]`; never check `[x]` without observed execution. |
| "The code is Python, so I should set PEP 8 as the coding standard." | Coding standards must be grounded in actual repo linter/formatter configuration, not assumed. | Ground in config files or label unconfigured patterns as proposals until approved. |
| "Every exception path is a business failure rule." | Language-level runtime type errors on hypothetical invalid constants are technical edge cases, not business rules. | Restrict failure modes to domain business logic and consistency invariants. |
| "GRACE_DAYS = 7 implies 7 calendar days and guaranteed thread-safety." | Terminology must not be strengthened beyond evidence; variable names do not guarantee concurrency safety. | State exact observed definitions; avoid adding 'calendar/business' or claiming unverified safety. |
## Red Flags - STOP and Ask
- Reading `README.md` or `docs/*.md` prose before legacy choices are answered.
- Citing excluded legacy documentation as evidence in feature specs.
- Overwriting or deleting files outside disclosed standard paths or specifically authorized replacements.
- Presenting code-derived observations as developer-endorsed requirements without evidence.
- Silently resolving a contradiction between code and documentation.
- Marking acceptance criteria as checked `[x]` without observed test execution.
- Inventing generic coding standards (e.g. PEP 8) without tooling configuration.
- Strengthening terminology (e.g. calendar/business days) or asserting unevidenced thread-safety.
- Elevating language runtime type errors into approved business failure rules.
- Generating documentation in a language other than English.
---

## Quick Reference: Two Legacy Choices

| Choice | Option | Meaning & Constraints |
|---|---|---|
| **Legacy Source** | Allowed | Inspect legacy docs; flag conflicts with code neutrally. |
| | Excluded (`no-source`) | Do NOT read or cite legacy docs for business rules. Derive only from code/schema. |
| **Write Mode** | Merge | Preserve existing content; update iteratively; request permission before preservation reads. |
| | Replace | Narrow replacement of disclosed standard paths and authorized nonstandard sources; leave undisclosed unique/ops docs untouched. |

---

## Detailed Standard Reference
See [references/project-knowledge-standard.md](references/project-knowledge-standard.md) for complete file layout, section requirements, and feature spec schemas.
