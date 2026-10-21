---
name: working-with-project-specs
description: Use when implementing features, fixing bugs, refactoring code, or resolving discrepancies in a repository with established project specifications, architecture documents, or engineering standards
---

# Working with Project Specs

## Overview

Locate affected specifications and local procedures before changing code. Draft missing known requirements immediately, preserve disputed existing rules, and hold only implementation dependent on unresolved behavior. Apply settled spec changes before dependent code/tests; preserve spec semantics during refactoring and use the host's coding lifecycle.

## When to Use

- Implementing a new feature in a repository with an established documentation tree (`docs/specs/`).
- Modifying behavior, fixing bugs, or addressing requirements governed by existing specifications.
- Refactoring code where existing business rules and behavioral semantics must be preserved.
- Encountering code that diverges from approved specification rules or documentation that contradicts code.

## When NOT to Use

- Scaffolding documentation formats or reorganizing selected docs without behavior changes (use `structuring-project-documentation`).
- Initializing documentation for an empty or un-implemented project (use `initializing-project-knowledge`).
- Reverse-engineering and establishing documentation for an existing project from scratch (use `documenting-existing-projects`).
- Performing a read-only audit of documentation integrity and code compliance without modifying code or specs (use `auditing-project-knowledge`).

---


## Phase 1: Progressive Contextual Reading

Do not read or force-load the entire repository documentation. Read only the documents directly relevant to the current task:

1. **Select specifications**: For business behavior, start at `docs/specs/README.md`, then read every affected capability spec and relevant dependencies. Follow overlapping-domain triggers; record unresolved selection scope instead of assuming one domain covers the task.
2. **Local workflow**: For behavior changes or discrepancies, read `docs/workflows/spec-changes.md` before mutation. Apply explicit decisions already supplied and the drafting/implementation boundary below.
3. **Architecture**: Read the relevant `docs/architecture.md` sections when module placement, dependencies, or runtime topology change.
4. **Engineering standards**: Read coding standards for implementation, testing standards for tests, and UI standards when interface behavior, styling, or accessibility is affected.
5. **Data model**: Read `docs/data-model.md` when persistent schemas or cross-domain relationships are affected.

**Done:** all affected behavior has a spec or a named gap; all applicable local routes have been followed before action.

---

## Phase 2: Confirmation & Discrepancy Gate (Mandatory Stop)

Separate drafting from implementation:
- **Missing specification**: Continue to Case A and write known requirements plus explicit Open Questions. Drafting does not require a separate sign-off.
- **Disputed existing requirements**: Preserve the disputed rules until the developer resolves them. Present the conflict using the formula below.
- **Unsettled affected behavior**: Hold dependent implementation and behavioral tests until a material decision is supplied. Continue independent work and documentation of settled facts.

**Done:** disputed existing rules remain intact, known missing content can be drafted, and each blocked implementation path names its required decision.

### Neutral Conflict Presentation
Present the discrepancy to the developer using this five-part structure:
1. **Approved Rule Statement**: Exact documented rule, source file, line reference, and rule ID (e.g. `BR-ADDON-001` in `docs/specs/billing/addon-purchase.md:24`).
2. **Observed Code Behavior**: Actual implementation and test behavior, source file, and line reference (e.g. `src/billing/addon.py:42`).
3. **Discrepancy Impact**: Concrete operational or business risks resulting from the divergence.
4. **Material Open Questions**: Specific ambiguities requiring clarification.
5. **Required Decision**: The explicit choice needed from the developer.

### Unaffected Work
If the user request contains independent, unaffected tasks (e.g. renaming an unrelated receipt label or updating copy):
- You may proceed with the unaffected task without blocking.
- You must still neutrally flag the background discrepancy in your response.
- Do NOT modify any code or tests related to the disputed business rule.

---

## Phase 3: Handling Approved Spec Changes

Use explicit contextual decisions already supplied. Apply the authorized delta to the authoritative specification first, then modify dependent implementation/tests and verify the affected acceptance criteria through the host lifecycle.

### Scope Discipline
Apply strictly the approved delta. Do NOT expand scope into neighboring rules, policies, or architecture:
- If developer approves removing subscription requirements for *addon purchase*, do **NOT** remove subscription requirements for *addon use* or change *addon pricing*.
- Keep all unapproved rules, constraints, and side effects strictly intact.

### Specification Update Protocol
When updating the feature spec (`docs/specs/<domain>/<feature>.md`):
- Before authoring, read the [feature-spec recipe](references/project-knowledge-authoring.md#feature-specifications) and its linked standard schema. A spec-only change needs that recipe, not the entire guide; if other documents are affected, consult their recipes as well. Keep generated project links self-contained and update the local spec index when selection scope changes.
- **Business Rules**: Update the specific rule (e.g. `BR-ADDON-001`) with clear, grounded wording.
- **Acceptance Criteria**: Format updated criteria as open conditions (`- [ ]`). Never mark criteria as checked (`- [x]`) until automated tests have been run and verified.
- **Data Model & Persistence**: Update the feature's ERD view if entity attributes or relationships changed. If repository-wide schema changes occurred, update `docs/data-model.md`.
- **Implementation & Test Mapping**: Verify and update links to real codebase files (`src/...`, `tests/...`).
- **No Change Archives**: Never create a `changes/` directory, proposal folder, or approval log. Updates belong directly in the authoritative spec files.

---

## Phase 4: Missing Specs vs. Behavior-Preserving Refactors

### Case A: Missing Specification (New Feature or Unspecified Behavior)
When requested to build a new feature or behavior where no specification exists:
- **Do NOT Skip Straight to Code**: Do not assume business rules from copyable code patterns or vague user phrases like "you know the flow."
- Read the [feature-spec recipe](references/project-knowledge-authoring.md#feature-specifications) and authoritative schema before drafting; use project evidence and explicit unknowns, not generic business rules.
- **Author a Durable Draft Spec**: Create the capability spec directly at `docs/specs/<domain>/<feature>.md`, following every section of the linked schema. Populate supplied requirements, identify unknown behavior in Open Questions, and mark unavailable implementation/test mappings honestly.
- **Placement**: Write directly into `docs/specs/<domain>/<feature>.md` using the shared metadata format. Never create proposal folders (`docs/proposals/` or `changes/`).
- **Behavioral Decisions**: Generate the specification without administrative sign-off. Resolve material open questions before implementing affected code; use explicit requirements already supplied.

### Case B: Behavior-Preserving Refactor
When refactoring code without changing observable business logic (e.g. extracting helper functions, optimizing database queries, improving readability):
- **Preserve Spec Semantics**: Do NOT rewrite or alter business rules, flows, or acceptance criteria in `docs/specs/`.
- **Mapping Updates Only**: Update `Implementation & Test Mapping` only if primary file paths or exported entrypoints were relocated or renamed.

---

## Phase 5: Delegation to Host Lifecycle

Do not create or impose an artificial second general coding lifecycle. Delegate routine implementation conventions to the project and runtime:
- **Coding Conventions**: Adhere to `docs/standards/coding.md` and repository linter/formatter configurations.
- **Testing Practices**: Follow `docs/standards/testing.md` and project test runners (e.g. pytest, vitest, cargo test).
- **Development Workflow**: Use the runtime's existing git, branch management, and code review practices.

## Completion

Reconcile every affected specification and implementation/test mapping, exercise the settled behavior through the host lifecycle, and report observed outcomes and remaining decisions. For behavior-preserving refactors, preserve spec semantics and update mappings only when their targets move. Shared schema and evidence rules live in the [Project Knowledge Standard](references/project-knowledge-standard.md#feature-spec-format).

---


