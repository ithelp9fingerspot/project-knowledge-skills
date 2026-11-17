---
name: working-with-project-specs
description: Use when implementing or changing a feature, fixing behavior, or refactoring in a repository governed by project specifications or engineering standards; not for read-only code exploration
metadata:
  tags: [specifications, documentation, requirements, software-development]
---

# Working with Project Specs

## Purpose

Locate affected specifications and local procedures before changing code. Create a spec for each new feature and update affected existing specs before dependent implementation. Draft known requirements immediately, preserve disputed existing rules, and hold only work dependent on unresolved behavior. Preserve spec semantics during behavior-preserving refactoring and use the host's coding lifecycle.

## Prerequisites

Use the repository's relevant specifications and engineering standards where available. Creating or updating a feature spec requires the bundled [authoring recipe](references/project-knowledge-authoring.md#feature-specifications) and [schema](references/project-knowledge-standard.md#feature-spec-format); no API keys or additional tools are required by this skill.

## Limitations

Specifications and incomplete documentation cannot settle missing or disputed business decisions. Record unknowns, preserve disputed rules, and hold only dependent work until the developer resolves them.

## When to Use

- Implementing a new feature in a repository with an established documentation tree (`docs/specs/`).
- Modifying behavior, fixing bugs, or addressing requirements governed by existing specifications.
- Refactoring code where existing business rules and behavioral semantics must be preserved.
- Encountering code that diverges from approved specification rules or documentation that contradicts code during an implementation task.

## When NOT to Use

- Exploring or explaining code read-only, without implementing or changing specifications.
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

### Troubleshooting Unavailable Guidance

**Project document missing or unreadable:** Record its path and investigate available project evidence. If the spec index is absent, enumerate the available `docs/specs/` tree and follow task-relevant links and cross-domain references. Inspect candidate specs for the affected capability, rules, and open questions; do not rely on a single feature-name match. Treat incomplete outlines as unverified, not authoritative. Record the candidates inspected and any inaccessible scope in the final report.

Treat a feature spec as missing only after the relevant available scope has been searched and no applicable spec found. If inaccessible files or unresolved ownership could contain an applicable rule, record the uncertainty and hold the work that depends on it rather than creating a competing spec. When local coding or testing standards are absent, use applicable repository configuration and established patterns, and report the gap.

**Bundled authoring recipe or schema unreadable:** Report the missing path and stop the spec-writing work that depends on it; do not invent a replacement format. Continue independent work that does not require that reference.

**Done:** all affected behavior has a spec or a named gap; all applicable local routes have been followed before action.

---

## Phase 2: Confirmation & Discrepancy Gate

Separate drafting from implementation:
- **Missing specification**: Continue to Case A and write known requirements plus explicit Open Questions. Drafting does not require a separate sign-off.
- **Disputed existing requirements**: Preserve the disputed rules until the developer resolves them. Present the conflict using the formula below.
- **Unsettled affected behavior**: Hold dependent implementation and behavioral tests until a material decision is supplied. Continue independent work and documentation of settled facts.

**Dependency test:** Split the request into concrete behavioral slices. A slice depends on an unresolved decision if plausible answers could change its externally observable inputs, outputs, errors, persisted state, events, or test expectations, including effects through shared code or data. Hold that slice and name the decision; proceed only with slices whose behavior and contracts remain valid under every plausible answer. If independence cannot be established, hold the uncertain slice. Report what proceeded and why, alongside the blocked slices and required decisions.

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

For each changed feature, update its authoritative specification with the authorized behavioral delta before modifying dependent implementation/tests. Use explicit contextual decisions already supplied; verify affected acceptance criteria through the host lifecycle.

### Scope Discipline
Apply strictly the approved delta. Do NOT expand scope into neighboring rules, policies, or architecture:
- If developer approves removing subscription requirements for *addon purchase*, do **NOT** remove subscription requirements for *addon use* or change *addon pricing*.
- Keep all unapproved rules, constraints, and side effects strictly intact.

### Specification Update Protocol
When updating the feature spec (`docs/specs/<domain>/<feature>.md`):
- Before authoring, read the [feature-spec recipe](references/project-knowledge-authoring.md#feature-specifications) and the [standard schema](references/project-knowledge-standard.md#feature-spec-format). A spec-only change needs those sections, not the entire guides; if other documents are affected, consult their recipes as well. Keep generated project links self-contained and update the local spec index when selection scope changes.
- **Business Rules**: Update the specific rule (e.g. `BR-ADDON-001`) with clear, grounded wording.
- **Acceptance Criteria**: Format updated criteria as open conditions (`- [ ]`). Never mark criteria as checked (`- [x]`) until automated tests have been run and verified.
- **Data Model & Persistence**: Update the feature's ERD view if entity attributes or relationships changed. If repository-wide schema changes occurred, update `docs/data-model.md`.
- **Implementation & Test Mapping**: Verify and update links to real codebase files (`src/...`, `tests/...`).
- **No Change Archives**: Never create a `changes/` directory, proposal folder, or approval log. Updates belong directly in the authoritative spec files.

---

## Phase 4: Missing Specs vs. Behavior-Preserving Refactors

### Case A: New Feature or Missing Specification
For each requested new feature, create its feature spec before implementing it. Apply the same workflow when changed behavior has no existing specification:
- **Do NOT Skip Straight to Code**: Do not assume business rules from copyable code patterns or vague user phrases like "you know the flow."
- Read the [feature-spec recipe](references/project-knowledge-authoring.md#feature-specifications) and [standard schema](references/project-knowledge-standard.md#feature-spec-format) before drafting; use project evidence and explicit unknowns, not generic business rules.
- **Author a Durable Draft Spec**: Create the capability spec directly at `docs/specs/<domain>/<feature>.md`, following every section of the linked schema. Populate supplied requirements, identify unknown behavior in Open Questions, and mark unavailable implementation/test mappings honestly.
- **Placement**: Write directly into `docs/specs/<domain>/<feature>.md` using the shared metadata format. Never create proposal folders (`docs/proposals/` or `changes/`).
- **Behavioral Decisions**: Use explicitly supplied requirements for the spec and their independent implementation and tests. Record material unknowns as Open Questions; resolve each before implementing or testing behavior that depends on it.

### Case B: Behavior-Preserving Refactor
When refactoring code without changing observable feature behavior (e.g. extracting helper functions, optimizing database queries, improving readability), use this case even if a spec for the existing feature is missing; do not create a spec solely for the refactor:
- **Preserve Spec Semantics**: Do NOT rewrite or alter business rules, flows, or acceptance criteria in `docs/specs/`.
- **Mapping Updates Only**: Update `Implementation & Test Mapping` only if primary file paths or exported entrypoints were relocated or renamed.

### Examples

```text
New feature: The developer specifies that customers can cancel an order but has not decided the deadline. Draft the cancellation spec with the supplied rule and an Open Question for the deadline. An unconditional cancellation endpoint depends on that decision because it would allow cancellation after a possible deadline; hold it. An unrelated receipt-label change can proceed if its behavior does not depend on the deadline. Report both boundaries.

Existing feature: The developer explicitly authorizes removing a subscription requirement for addon purchase. Update that purchase rule and its acceptance criteria in the existing spec before changing code and tests. Preserve the separate addon-use and pricing rules.
```

---

## Phase 5: Delegation to Host Lifecycle

Do not create or impose an artificial second general coding lifecycle. Delegate routine implementation conventions to the project and runtime:
- **Coding Conventions**: Adhere to `docs/standards/coding.md` and repository linter/formatter configurations.
- **Testing Practices**: Follow `docs/standards/testing.md` and project test runners (e.g. pytest, vitest, cargo test).
- **Development Workflow**: Use the runtime's existing git, branch management, and code review practices.

## Completion

Reconcile every affected specification and implementation/test mapping, exercise the settled behavior through the host lifecycle, and report observed outcomes and remaining decisions. For behavior-preserving refactors, preserve spec semantics and update mappings only when their targets move. Shared schema and evidence rules live in the [Project Knowledge Standard](references/project-knowledge-standard.md#feature-spec-format).

---


