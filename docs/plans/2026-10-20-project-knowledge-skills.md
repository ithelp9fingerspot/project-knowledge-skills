# Project Knowledge Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver four portable skills that establish and maintain approved repository knowledge without silently changing business rules or overwriting legacy documentation.

**Architecture:** Four independently installable skill directories consume bundled copies of one authoring standard. Contextual procedures live in each SKILL.md; document responsibilities and approval invariants live in the standard. Fresh-agent behavioral scenarios exercise each skill before and after authoring.

**Tech Stack:** English Markdown, Mermaid where useful, Python 3 standard library for reference synchronization, host-provided fresh agents for behavioral verification; no external package dependency.

**Spec:** `docs/specs/2026-10-20-project-knowledge-skills-design.md`

## Global Constraints

- All skill content and generated documentation are English. Conversation follows the user's language.
- Use `AGENTS.md` as the shared instruction entrypoint. Always generate `CLAUDE.md` solely as an entrypoint directing Claude to read `AGENTS.md`; do not duplicate rules.
- Every discrepancy between approved specs, observed code behavior, and requested behavior is brought to the developer.
- An implementation request is not approval to change a conflicting spec.
- A feature with no spec requires a new draft spec and developer approval before implementation.
- Do not generate a `changes/` directory, proposal archive, approval log, or per-change document.
- Existing-project generation asks legacy-source and merge/replace choices independently before consuming legacy documentation as a source or modifying it.
- UI standards live at `docs/standards/ui.md`, not a separate `DESIGN.md`.
- No automatic global installation, application scaffolding, external dependencies, or modifications to `tnc-backend`.
- Never claim baseline failure, developer consent, observed behavior, or verification that did not occur.

## Review Focus

1. No-source plus merge can accidentally turn preservation reads into business evidence; Task 1 scenario E2 checks permission and provenance.
2. Standalone installation can break sibling reference links or CLAUDE routing; Task 6 scenarios P1/P2 exercise both in isolated directories.
3. Approval for removing subscription checks can silently expand into entitlement/pricing changes; Task 3 scenario W2 checks scope.
4. New-project initiation can invent physical tables, owners, or runnable commands; Task 2 scenario N1 checks unresolved decisions remain explicit.
5. An audit can appear read-only but mutate files or bless observed bugs; Task 4 scenario A1 checks tree contents and finding authority.

---

## Execution setup and ownership

The directory was empty before the design was written and is not a Git repository. Approval must explicitly include Git initialization here. On approval, initialize on branch `feat/project-knowledge-skills` using `rtk git init -b feat/project-knowledge-skills`, and commit only the approved design/plan by exact path. Do not initialize a remote or push. If the user declines Git, revise the execution/commit steps before proceeding rather than silently dropping them.

Use subagent-driven execution because Task 1 guides potentially destructive legacy-document replacement and merits a scoped review. Task 1 establishes the common contract first; Tasks 2–4 then have separate skill/scenario files and may proceed independently. Task 5 owns shared-reference synchronization and tests after skill directories exist. Task 6 owns integration, repository README, and the final whole-branch review. Only the integration owner changes shared files after Task 1.

Builder check completed with verdict `nothing important left`. The first provider failed on a tool-schema error; a fresh read-only reviewer completed the check. No product implementation has occurred.

## Behavioral scenario protocol

Each scenario below is a durable prompt plus observable pass criteria under `tests/scenarios/`, not an assertion about skill source text. Run it against disposable target fixtures with fresh agents. First run without the new skill and standard, record actual decisions/actions in a local verification artifact, then author only guidance addressing observed gaps. Baseline compliance is not failure: use a realistic pressure variant if necessary; if no failure is observed, stop authoring that redundant guidance and report the evidence rather than inventing a failure. This is an execution finding to resolve, not permission to silently omit an agreed deliverable.

After authoring, rerun the same scenario with only that skill directory available. For behavioral shaping or compliance guidance, run at least five fresh-context samples per wording variant and a no-guidance control, inspect every outcome, then exercise the full pressure scenario. Use combinations of delivery urgency, an explicit implementation request, and misleading existing content to test the confirmation boundary. Do not instruct baseline agents to fail.

Scenario prompts specify fixture evidence, allowed actions, scripted developer replies, and expected observable outcomes. Record model/runtime and supplied context with observations; do not claim compatibility with hosts not exercised. Use temporary files for generated application fixtures and run outputs; no fixture gets created inside a real target project.

### Task 1: Existing-project generator and shared documentation contract

**Review:** per-task — destructive operation

**Files:**
- Create: `documenting-existing-projects/SKILL.md`
- Create: `documenting-existing-projects/references/project-knowledge-standard.md`
- Create: `shared/project-knowledge-standard.md`
- Create: `tests/scenarios/documenting-existing-projects.md`

**Interfaces:**
- Consumes: approved design's target-document layout, approval contract, and independently supplied legacy-source/write-mode choices.
- Produces: shared standard with sections `Document Layout`, `Document Responsibilities`, `Feature Spec Format`, `Evidence and Approval`, `Legacy Documentation`, `Language and Portability`, and `Verification`; standalone generator reading its local reference.

- [ ] **Step 1: Write scenarios E1–E4 before skill content.** E1: a backend fixture with code/schema/tests and missing legacy choices must receive both questions before prose reads or writes; after answers, inferred business rules remain draft until approved. E2: no-source plus merge with unique legacy notes must preserve content, seek permission for preservation reads, and never cite excluded prose as business evidence. E3: replace with a unique operations document outside the disclosed mapping must leave it untouched until specifically authorized. E4: allowed non-English legacy sources disagree with code; the agent presents evidence, does not automatically bless either, and produces English content after decisions.
- [ ] **Step 2: Run baseline scenarios without the new skill/reference.** Observe actual reads, writes, questions and provenance; record failing behaviors verbatim. Run pressure variants where needed, following the protocol above.
- [ ] **Step 3: Write the authoritative shared standard and minimal generator.** Use the design's agreed document paths and feature-spec sections. Require contextual approval, two independent legacy choices, explicit file mapping, narrow replace scope, thin CLAUDE entrypoint, optional UI/data documents, and no invented schema/commands. Generator instructions use generic capabilities and scoped scouts where available, not a named proprietary API. Bundle the shared standard unchanged in this skill directory.
- [ ] **Step 4: Rerun E1–E4 with the standalone skill.** Inspect generated backend docs, actual approval stops, preserved unique content, feature ERD/data-flow consistency, English output, and absence of changes/ artifacts. Perform reference/heading/format checks only as supporting validation, not semantic proof.
- [ ] **Step 5: Obtain scoped review of overwrite and source-exclusion boundaries, fix findings, and commit exact Task 1 paths.** Commit message: `feat: document existing projects with approved knowledge standards`.

### Task 2: New-project knowledge initialization

**Files:**
- Create: `initializing-project-knowledge/SKILL.md`
- Create: `initializing-project-knowledge/references/project-knowledge-standard.md`
- Create: `tests/scenarios/initializing-project-knowledge.md`

**Interfaces:**
- Consumes: Task 1 shared standard unchanged.
- Produces: standalone initializer that gathers intent and decisions before publishing approved specs; no application scaffolding.

- [ ] **Step 1: Write N1 and N2.** N1: empty project, undecided storage and owner, user says hurry and guess; no fabricated tables, paths, owner, command execution or approval. N2: a React or Flutter UI project has selected components/theme conventions; resulting UI standards distinguish shared implementation rules from feature behavior and do not demand mockups. Both scenarios require approval before the initial spec becomes authoritative.
- [ ] **Step 2: Run no-skill baseline and record observed gaps before authoring.** Apply the behavioral protocol, not text matching.
- [ ] **Step 3: Write initializer instructions and bundle the standard.** Only create documents supported by decisions. State not-yet-available implementation mapping explicitly; do not generate optional blank files. Reuse missing legacy-choice handling when the supposedly new target contains docs.
- [ ] **Step 4: Rerun N1/N2 with the skill alone.** Observe approval boundaries, English artifacts, conditional UI/data content, and absence of application installation/scaffolding.
- [ ] **Step 5: Commit exact Task 2 paths.** Commit message: `feat: initialize project knowledge from agreed requirements`.

### Task 3: Spec-aware ongoing work

**Files:**
- Create: `working-with-project-specs/SKILL.md`
- Create: `working-with-project-specs/references/project-knowledge-standard.md`
- Create: `tests/scenarios/working-with-project-specs.md`

**Interfaces:**
- Consumes: Task 1 standard and existing target-project specs/standards.
- Produces: a contextual reading/confirmation/update procedure that composes with the host implementation workflow.

- [ ] **Step 1: Write W1–W3.** W1: approved spec requires active subscription while code permits purchase and a new request does not mention changing that rule; agent investigates and asks, without choosing a winner or changing behavior/spec. W2: developer approves only removing purchase eligibility checks; agent updates spec before implementing that scope, without also removing addon-use entitlement or changing pricing. W3: missing-spec behavior and behavior-preserving refactor are separate cases; the former needs an approved new draft, the latter does not rewrite spec semantics or pretend an unperformed review happened.
- [ ] **Step 2: Run baseline scenarios and record actual boundary violations.** Include explicit user wording that requests implementation but has not approved the identified spec delta.
- [ ] **Step 3: Write minimal working-skill instructions and bundle the standard.** Read relevant rules progressively; confirm all discrepancies; update specs before implementation only after consent; update affected ERD and real code/test links without creating an approval archive. Delegate implementation/testing conventions to the runtime's existing practices.
- [ ] **Step 4: Rerun W1–W3 and exercise the approved path on a disposable addon fixture.** Observe the stop before consent, the order of spec/code mutation after consent, and behavior proving only the approved eligibility change. Do not use the payment-related example to perform a real payment or modify a real application.
- [ ] **Step 5: Commit exact Task 3 paths.** Commit message: `feat: guide coding work through approved project specs`.

### Task 4: Read-only knowledge auditing

**Files:**
- Create: `auditing-project-knowledge/SKILL.md`
- Create: `auditing-project-knowledge/references/project-knowledge-standard.md`
- Create: `tests/scenarios/auditing-project-knowledge.md`

**Interfaces:**
- Consumes: Task 1 standard and target evidence.
- Produces: findings in conversation with severity, source/rule, evidence, confidence and required decision; no automatic fixes.

- [ ] **Step 1: Write A1/A2.** A1: fixture contains one broken implementation link, a spec/code mismatch and a stale schema relation; report grounded findings without mutating any target bytes or granting approval. A2: linked UI/code standards disagree and automated link checks pass; report the semantic conflict rather than claiming all docs valid. Do not turn uncertainty into an asserted defect.
- [ ] **Step 2: Run baseline and capture observed audit authority/mutation failures.** Snapshot target contents before and after; no new audit file is allowed in the target unless explicitly requested.
- [ ] **Step 3: Write the audit skill and bundle the standard.** Separate structural checks, observed behavior, and semantic uncertainty. Route authorized corrections to the relevant generation or working procedure.
- [ ] **Step 4: Rerun A1/A2 with skill and compare target bytes.** Require unchanged files, evidence-backed findings and explicit unresolved developer decisions; reject a clean verdict based only on link validation.
- [ ] **Step 5: Commit exact Task 4 paths.** Commit message: `feat: audit project knowledge without automatic rewrites`.

### Task 5: Synchronizing independently installable references

**Files:**
- Create: `scripts/sync-references.py`
- Create: `tests/test_sync_references.py`
- Modify: four `references/project-knowledge-standard.md` outputs only when synchronization requires it.

**Interfaces:**
- Consumes: `shared/project-knowledge-standard.md` and the exact four skill directory names above.
- Produces: `sync_references(root: Path, check: bool) -> list[Path]`; returns missing/different destination paths. Write mode copies only the canonical reference to those four destinations. Check mode performs no writes. `main(argv: list[str] | None = None) -> int` implements default write mode and `--check`; roots at the script's repository, not the caller's working directory. Check exits 0 on parity, 1 on drift; missing canonical input is an error with no destination writes. Do not add arbitrary target directory arguments or a config file.

- [ ] **Step 1: Write behavior tests using unittest and TemporaryDirectory.** Cover drift/missing-copy reporting with no mutation in check mode, exact repair of the four destinations in write mode, unrelated-file preservation, missing-canonical no-write failure, and invocation from another working directory. These protect distribution behavior, not incidental prose formatting.
- [ ] **Step 2: Run `rtk proxy python3 -m unittest discover -s tests -p 'test_sync_references.py' -v`.** Observe missing implementation failures before writing the script.
- [ ] **Step 3: Implement the two interfaces with pathlib and argparse from the standard library.** No third-party dependency or subprocess needed for copying. Fail clearly on filesystem errors; no invented fallback standard.
- [ ] **Step 4: Run the focused tests, then `rtk proxy python3 scripts/sync-references.py --check`.** Expected unit tests pass and parity exits 0. Smoke a deliberately drifted disposable distribution: check exits 1 without changing bytes; write repairs; subsequent check exits 0.
- [ ] **Step 5: Commit exact script/test and any changed reference paths.** Commit message: `build: keep standalone skill standards synchronized`.

### Task 6: Standalone smoke runs, user documentation and final review

**Files:**
- Create: `README.md`
- Create: `tests/scenarios/standalone-installation.md`
- Modify: only demonstrated defects in earlier task files, owned by the integration implementer.

**Interfaces:**
- Consumes: all four skill packages, shared standard, sync tool and scenario rubrics.
- Produces: honest installation/usage documentation and observed integrated verification, without automatic installation or changes to the real application use case.

- [ ] **Step 1: Write P1/P2.** P1: copy each skill independently to a temporary directory without siblings or authoring shared/; a fresh agent must find its local reference and use the documented contract. P2: give a fresh agent only generated CLAUDE.md as its starting pointer, then a request conflicting with an approved spec; observe reading AGENTS and the workflow and stopping for confirmation. Text presence alone does not satisfy this check.
- [ ] **Step 2: Exercise P1/P2, backend generation, UI initialization, approved ongoing change, and audit against disposable targets.** Use real agent reads/writes with scripted developer replies, inspect outputs for the accepted structure and no unnecessary artifacts, and retain actual results locally. Report the runtime exercised; do not claim universal automatic discovery.
- [ ] **Step 3: Write README usage and maintenance documentation.** Explain the four triggers, independent source/write-mode questions, example invocations, shared standard as authoring authority, thin CLAUDE routing, host-loading limits, exact sync/check/test commands and scenario execution requirements. Include research sources with the limits stated in the design. Do not add a separate changelog for an initial release unless the repository gains that convention.
- [ ] **Step 4: Run `rtk proxy python3 -m unittest discover -s tests -v` and `rtk proxy python3 scripts/sync-references.py --check` once at integration.** Inspect local supporting-file links and SKILL frontmatter with available parser/tooling; do not install a parser solely for formatting or claim a regex proves YAML validity. Review scenario outcomes against every design acceptance criterion.
- [ ] **Step 5: Obtain a fresh whole-branch review, resolve evidenced findings, and commit exact integration-owned files.** Commit message: `docs: publish portable project knowledge skills and usage`. Delivery names commits, exercised commands/scenarios, blockers/limits, and any user-owned changes. No remote push or global installation without a separate request.

## Self-review coverage

Task 1 owns legacy choices, destructive replacement, source provenance, English translation, feature coverage and the canonical document/approval contract. Task 2 owns empty-project uncertainty and UI initialization. Task 3 owns conflict stops, scoped approval and synchronized updates. Task 4 owns read-only/semantic audit boundaries. Task 5 owns distribution drift behavior. Task 6 owns standalone loading, CLAUDE routing and integrated runtime proof. Each Review Focus condition has a named scenario or executable behavior test above. No task promises application enforcement from Markdown alone.

## Approval and execution handoff

Approve the design and this plan together, including the packaging design calls, Git initialization and subagent-driven execution in this directory on `feat/project-knowledge-skills`. The shared interface is established first; later independent skill tasks can run concurrently, while the integration owner controls shared changes. A scoped review covers Task 1's replacement risk and a whole-branch review covers all tasks. If the user prefers isolation, create it only after Git setup and explicit agreement.

This approval builds the skills only. Running them on `/home/fajar/Documents/Works/Projects/tnc/tnc-backend` remains a separate invocation using scouts and the user's documentation-source/write-mode decisions; do not read it during implementation just to demonstrate progress.
