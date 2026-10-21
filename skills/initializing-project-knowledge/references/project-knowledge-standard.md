# Project Knowledge Standard

Authoritative specification for repository documentation structure, document responsibilities, feature specification format, evidence requirements, approval boundaries, and legacy documentation handling.

---

## Document Layout

Every documented repository uses a standardized, modular documentation tree. Content authoring creates files supported by evidence or explicit decisions. Explicit format-only requests follow the [Documentation Structuring](#documentation-structuring) contract instead.

```text
README.md
AGENTS.md
CLAUDE.md
docs/
  README.md
  project.md
  architecture.md
  data-model.md                 # when persistent data exists
  development.md
  standards/
    coding.md
    testing.md
    ui.md                       # when user interface exists
  workflows/
    spec-changes.md
  specs/
    README.md
    <domain>/
      <feature>.md
```

### Optional Documents
- `docs/decisions/`: Created only when a durable technical architectural decision warrants an Architecture Decision Record (ADR). Initial architectural rationale belongs in `docs/architecture.md`. For ADR authoring and numbering, read the [ADR recipe](project-knowledge-authoring.md#architecture-decision-records).
- `docs/data-model.md`: Created only when the project stores persistent data.
- `docs/standards/ui.md`: Created only when the project contains a user interface.
- Do not create a `changes/` directory, proposal archive, approval log, or per-change documentation artifacts.

### File Naming
Keep discovery filenames exact: `README.md`, `AGENTS.md`, `CLAUDE.md`, and skill entrypoint `SKILL.md`. Other documentation uses lowercase kebab-case names matching its context. Keep cross-language conventions in `docs/standards/coding.md`; disclose substantial language or boundary-specific guidance through files such as `docs/standards/typescript.md` or `docs/standards/api.md` only when needed. Each topic has one owner and a task-conditioned pointer. These companion names confer no automatic loading behavior. Preserve existing names unless a scoped rename and its link updates are authorized.

## Documentation Structuring

Structuring creates outlines or reorganizes selected documentation without investigating implementation. Use the same document recipes as content authoring; select only the requested files and applicable sections. With no file selection, start with the three root entrypoints plus `docs/README.md`, `docs/project.md`, `docs/architecture.md`, and `docs/development.md`.

Choose source depth from the request:
- **Outline-only**: Inventory filenames and headings of selected sources. Use their topics to organize the framework; leave prose claims uncopied.
- **Selected-content reuse**: Read each selected section completely before retaining or moving its content. Record the source path/section and that implementation validation was not performed beside reused claims. Preserve meaning, identifiers, caveats, and uncertainty; report contradictions instead of resolving them.

When depth is unspecified, use outline-only. When existing docs are requested as a basis but no source is named, inventory filenames and ask which sources may be inspected; broader legacy prose is outside that permission. Host-required agent instructions remain mandatory. Application source, schemas, tests, and unrelated documents remain outside discovery; manifests may be inspected only when needed to select applicable formats.

Create missing destinations by default and preserve all existing files. Updating an existing destination requires explicit scoped authorization and reading the complete affected section; replacing a whole document requires reading the whole document. Disclose source-to-destination mapping and any collisions before mutation. Keep source files intact unless relocation or deletion is separately authorized. The general legacy source and write-mode gates below apply to content discovery; this bounded structuring contract supplies the corresponding source/write limits without requiring code investigation or business approval.

Outlines use the recipe's headings and short English filling prompts. At the top of every unfinished content document, before substantive content, write `Documentation outline; project content is incomplete and is not an implementation specification.` Follow it with `Action required: Fill the marked sections with project-specific evidence or explicit decisions before using them as requirements or operational instructions.` This applies to partially filled and merged documents too: mark each unfinished section `Needs project input:` with the specific information to supply; distinguish reused, implementation-unvalidated passages from confirmed content. Examples, placeholders, and filling prompts establish no project facts, commands, policies, or business approval. Retain the notice until all filling prompts in that document are resolved; confirmed sections remain usable only within their stated evidence boundaries.

Build usable navigation to actual files and label every unfinished destination `incomplete outline` in indexes and task routes. `AGENTS.md` must explain that linked outlines are not authoritative requirements or executable procedures: obtain the missing project input before acting on an affected section, while independent confirmed work may proceed. These safety/navigation instructions are operative even when project guidance is incomplete. `CLAUDE.md` remains exactly its one-line import; the warning belongs in AGENTS and unfinished content documents, not in CLAUDE. Create conditional UI/data-model/ADR/context standards or named feature outlines only when explicitly selected or their applicability is known; a template request does not imply every optional file. Template field labels remain instructional, not fabricated values or approvals.

Structuring is complete when every scoped destination has its applicable headings, each reused passage retains its source and caveats, every link/import resolves, and preserved files remain unchanged. Report outlines versus reused content and explicitly state that code/spec alignment was not checked. Filling and validating content uses the appropriate authoring or audit workflow; the presence of an outline does not constitute a completed knowledge base.

---

## Document Responsibilities

Each document has a distinct scope and purpose. Avoid duplicating information across documents; link to the authoritative source instead.

When writing or auditing a document, read its recipe in the [Authoring Guide](project-knowledge-authoring.md). Use the recipe's exact English section names and relative order, with project-specific contents or the explicit structuring contract's filling prompts. Include conditional sections only when applicable; name concrete unknowns for unresolved content rather than inventing facts. Additional project-specific subsections may elaborate the relevant standard section. The feature-spec schema below remains authoritative for feature headings and fields.

Generated project documentation is self-contained: local links resolve inside the project, not to installed skills or this skill repository. Transfer necessary spec-format guidance into the project's spec index and workflow. External product/API documentation links remain permitted.

### Root Entrypoints
- `README.md`: Concise introduction to the repository, its purpose, target audience, and direct links to setup instructions (`docs/development.md`) and project documentation (`docs/README.md`).
- `AGENTS.md`: Mandatory instructions for AI coding agents. Functions as a concise navigation map, setting out contextual reading paths, stop/confirmation rules, and links to technical standards and spec workflows. Keep it compact; do not dump full manuals into this file.
- `CLAUDE.md`: Contains exactly the single line `@AGENTS.md` (a final newline is allowed). This Claude-specific import loads the shared instructions; `AGENTS.md` owns their content.

### Project & Architecture
- `docs/README.md`: Task-oriented documentation index and reading guide for human developers and agents navigating the knowledge base.
- `docs/project.md`: High-level business purpose, user personas, domain glossary, and technology stack overview. Links directly to package manifests and configuration files rather than manually copying dependency versions.
- `docs/architecture.md`: System design, module responsibilities, architectural boundaries, dependency flows, and architectural rationale. Its `Repository Map` section owns the annotated project structure and change-placement guidance; root entrypoints link there instead of copying trees.
- `docs/data-model.md`: Repository-wide entity-relationship overview, core entity definitions, storage engines, and links to physical schemas or migrations. Break large models into domain diagrams.

### Development & Standards
- `docs/development.md`: Prerequisites, local setup, supported invocation procedures, environment variable names (never secret values), test execution, and troubleshooting. Tooling owns command definitions; this document explains their use, sequencing, and non-obvious requirements. Other documents link here instead of repeating commands.
- `docs/standards/coding.md`: Language-specific and framework-specific implementation patterns, naming conventions, and error-handling conventions grounded in repository configuration and linters. Do not invent generic conventions (e.g. PEP 8, generic style guides) from small fixtures; label unconfigured patterns as proposals until approved.
- `docs/standards/testing.md`: Testing strategy, actual test layers, fixture/isolation conventions, assertion styles, and meaningful failure coverage. Link to `docs/development.md` for execution commands and prerequisites.
- `docs/standards/ui.md`: Component conventions, styling/theming systems, layout patterns, interaction states, accessibility requirements, and code patterns. Does not demand mandatory screen mockups.

### Workflows & Specifications
- `docs/workflows/spec-changes.md`: Lifecycle procedure for proposing, approving, implementing, and verifying feature specification changes.
- `docs/specs/README.md`: Task-oriented index of feature specifications grouped by domain, explaining the feature specification format and lifecycle. Distinguish overlapping domain triggers and select all affected specs rather than imposing a one-spec-only limit.

---

## Feature Spec Format

### Capability Boundaries

A domain groups specifications; each feature spec owns one capability with a distinct trigger, observable outcome, rules, and acceptance criteria. Use `authentication/login.md` and `authentication/register.md`, not a single authentication overview as their substitute. Create only capabilities supported by permitted evidence or supplied requirements.

Group endpoint/function steps when they form one cohesive outcome: password-reset request and completion can share `authentication/password-reset.md`, with both stages and their branches explicit. Split independently meaningful capabilities; endpoint count alone does not determine file count. Shared terms and technical mechanisms remain in their owning project/architecture/standards documents, linked rather than copied into every capability.
Login, logout, and session refresh have independently observable outcomes and remain separate capability specs even though they share session machinery. A shared lifecycle or domain label alone is not a grouping rationale; group stages only when they jointly complete one outcome, and preserve each stage's flows and failures.

For existing-project discovery, account for every in-scope capability found through entrypoints, routing, services, schemas, and tests: map it to a spec, justify grouping it with another capability, or report the specific untraced path. An overview or sample flow does not establish complete domain coverage. Track this internally and summarize gaps in conversation; no discovery artifact is required in the target.

### Required Sections


Feature specifications live under `docs/specs/<domain>/<feature>.md`. Every feature spec adheres to a consistent structure. If a section does not apply (e.g. no persistent data), state that concisely rather than inventing details.

```markdown
# [Feature Name]

## Metadata
- **Domain**: [Domain name]
- **Last Updated**: [Actual write date, filled automatically]
- **Related Specs**: [Links to related specs, or None]

## Purpose & Scope
Concise summary of the feature, target user problem, and explicit out-of-scope boundaries.

## Domain Glossary
Feature-specific terms and definitions aligned with `docs/project.md`.

## Business Rules
Numbered rules with stable identifiers:
- **BR-[DOMAIN]-[001]**: [Rule statement]
- **BR-[DOMAIN]-[002]**: [Rule statement]
*Precision rules*:
- Ground rules in permitted evidence plus explicit developer decisions, distinguishing observed implementation from intended behavior. Do not strengthen terminology beyond evidence (e.g. do not turn `GRACE_DAYS = 7` into "calendar days" or "business days" without explicit backing).
- Distinguish return values from side effects (e.g. an evaluation returning `True` does not mean an entity was cancelled or persistence updated).
- Do not assert unevidenced architectural guarantees (e.g. thread-safety, distributed atomicity) from identifiers alone.
## Data Model & Persistence
ERD view relevant to this feature (view of the shared data model, not a disconnected schema).
- Entities, table roles, key columns, and constraints.
- (If no persistent data, state: "No persistent data.")

## Flows & Data Access
For every evidenced or explicitly required flow, state actor/trigger, inputs and prerequisites, then numbered steps separating validation, data reads, state transitions, writes, side effects, and observable outcomes. Describe alternate branches and their conditions explicitly; cite their implementation/test sources when reconstructing existing behavior. Distinguish unknown ordering or effects from established behavior.

## Failure Modes & Consistency
- Domain validation failures and boundary cases: triggering condition, caller-visible result, and resulting state, including partial-failure effects supported by evidence.
- Derive failure claims from evidenced domain behavior; distinguish runtime mechanics from business requirements.
## Acceptance Criteria
Observable, verifiable criteria formatted as open conditions:
- [ ] Criterion 1
- [ ] Criterion 2
*Invariant*: Acceptance criteria are required conditions, NOT execution logs. Never mark criteria as checked `[x]` without observed, verified test execution.
## Contracts & Dependencies
- External APIs, message payloads, webhooks, or service interfaces.

## Implementation & Test Mapping
Links to real codebase files:
- **Implementation**: `src/...`
- **Tests**: `tests/...`
*(When authoring for an unimplemented feature, explicitly state: "Not yet available.")*

## Open Questions
- Unresolved behavioral questions requiring a developer decision. Record them without blocking generation of the known content; resolve affected in-scope questions before implementing that behavior. Excluded future topics do not block current work.
```

### Generation and Change Boundaries
Generate the requested documentation directly from permitted evidence and supplied requirements. Fill derivable metadata automatically: domain from feature scope/path, Last Updated from the actual write date, and related-spec links from discovered relevant files. Feature specs omit Status, Owner, and Last Reviewed; use Git/PR history for review provenance. Routine refactors do not refresh spec dates when the spec content is unchanged.
Required headings are coverage prompts, not permission to invent contents. Without evidence or a supplied decision for persistence, field names, services, validation outcomes, or side effects, state the specific unknown in that section and Open Questions. Keep unresolved in-scope behavior in scope; only explicit scope decisions establish exclusions. A requested capability does not imply tables, identifier formats, notifications, or default failure semantics.

Generation itself needs no owner assignment, review checklist, status transition, or blanket sign-off. Describe code-derived claims as observations and place unresolved behavioral decisions in Open Questions; a generated file does not assert developer endorsement. Ask only for missing source/write permission, destructive changes, or a material decision that cannot be derived. Implementation of disputed or unspecified behavior still requires a decision; proceed with independent generation work meanwhile.
---

## Evidence and Approval

### Evidence Hierarchy
1. **Code Implementation**: Primary evidence of current operational behavior. Does not automatically prove approved business intent.
2. **Automated Tests**: Primary evidence of developer test expectations and regression assertions. Does not constitute business approval.
3. **Database Schemas & Migrations**: Primary evidence of physical persistence structure and database constraints.
4. **Configuration & Tooling**: Primary evidence of runtime parameters, build commands, and lint rules.
5. **Legacy Documentation**: Historical evidence. May be used as a source only with explicit developer permission.

### Approval Rules
- **Explicit Consent**: Developer approval must be explicit and contextual. Never assume, infer, or fabricate approval.
- **Conflict Presentation**: When code, tests, legacy docs, or user requests disagree, present the discrepancy neutrally:
  1. Approved rule or documented statement (with source and line reference).
  2. Observed code or test behavior (with file and line reference).
  3. Known impact or risks.
  4. Material open questions.
  5. Specific decision required from the developer.
- **No Unilateral Blessing**: Do not bless code over documentation or documentation over code simply because code is newer or tests pass.
- **Scope Discipline**: Approval for a specific change (e.g. modifying a grace period) does not authorize modifying related pricing, cancellation policies, or architecture.
- **Grounded Precision**: Inferred specifications must not invent generic conventions, elevate language type errors to business rules, invent unevidenced guarantees, or mark acceptance criteria `[x]` without observed test execution.
---

## Legacy Documentation

Existing repositories often contain documentation (`README.md`, `docs/`, wiki pages, runbooks). The agent must respect developer choices regarding these files.

### Two Independent Choices
Before reading legacy prose for business meaning or writing/modifying any files, the agent must ask two independent choices (batched together if missing):
1. **Legacy Source Choice**: May existing legacy documentation be used as an additional reference source for business rules and intent?
2. **Write-Mode Choice**: Should new documentation **merge** with existing documentation, or **replace** existing documentation?

### Handling Source Choices
- **Allowed as source**: Legacy documentation may be consulted alongside code, schema, and tests. Discrepancies between legacy prose and code must be presented as conflicts for developer resolution.
- **No-source (excluded)**: Legacy documentation must NOT be read or cited as evidence of business intent or requirements. Feature specs and architecture must be derived strictly from code, schema, configuration, and developer answers.

### Handling Write-Mode Choices
- **Merge Mode**:
  - Preserve unique content and meaning, not obsolete layout. Every authorized merged destination follows the current document recipe's headings, order, and content boundaries; do not merely append the new template beneath legacy sections.
  - For `AGENTS.md`, apply the [AGENTS recipe](project-knowledge-authoring.md#agentsmd). Resolve contradictory instructions with the developer; format normalization does not authorize changing project policy.
  - Before writing, account for each unique source rule, caveat, command, reference URL, and runbook step and its destination. Compare the final text against that inventory: retain exact thresholds, qualifiers, consent requirements, and prohibitions; a shorter paraphrase must not weaken them. Keep granular rules verbatim when equivalence is uncertain. Remove only actual duplication, never unique content to meet the line budget. Use this accounting internally and report any unresolved item; no target-repository audit artifact is required.
  - If `no-source` was chosen, legacy files may be read **only for preservation purposes** (to avoid losing unique operational content or custom guides). The agent **must ask explicit permission** before reading legacy files for preservation, clearly stating the preservation purpose.
- **Replace Mode**:
  - Narrow replacement scope: Replacement applies strictly to disclosed standard destination paths corresponding to the standard documentation layout (`README.md`, `AGENTS.md`, `CLAUDE.md`, standard `docs/` paths) plus individually disclosed, specifically authorized nonstandard sources being replaced or relocated into the standard structure.
  - Never run blanket deletions (e.g. `rm -rf docs/` or directory wipes).
  - Undisclosed, out-of-scope, or unique documents (e.g. `docs/compliance/`, `docs/ops-manual.md`, audit notes) must be left completely untouched unless specifically authorized by the developer.
---

## Language and Portability

### Language Policy
- **Generated Documentation**: All generated documentation files (`README.md`, `AGENTS.md`, `CLAUDE.md`, and all `docs/**/*.md` files) must be written in **English**.
- **Conversation**: The agent converses in the language preferred by the user.
- **Preserved Identifiers**: Preserve code identifiers (class names, function names, variables, routes), error strings, and domain terminology exactly as they appear in code. Confirm uncertain translations with the developer.

### Portability Guidelines
- The generated documentation must be portable across general AI coding agents (Claude, Gemini, Copilot, Codex, etc.).
- Shared documentation uses ordinary Markdown and relative links without proprietary tools, MCP servers, or custom configuration requirements.
- `CLAUDE.md` is the intentional runtime-specific exception: use its exact import recipe. Other agents enter through `AGENTS.md`; ordinary document pointers remain task-conditioned links rather than eager imports.

---

## Verification

Before declaring documentation generation complete, verify:
1. **Link Integrity**: All relative Markdown links resolve to existing files; every `CLAUDE.md` import resolves to its adjacent `AGENTS.md` and matches the exact entrypoint recipe.
2. **Reading Route**: Starting at `CLAUDE.md`, follow `AGENTS.md` task conditions to the actual architecture, affected spec, and execution destinations as applicable; verify files and section anchors, including overlapping-domain routes.
3. **Data Model Consistency**: Ensure feature ERDs reflect the shared application data model in `docs/data-model.md` without contradictory relationships.
4. **Evidence Integrity**: Distinguish implementation observations, stated requirements, and unresolved behavioral questions without administrative lifecycle fields or fabricated endorsement.
5. **No Invented Artifacts**: Verify no temporary discovery files, `changes/` folders, or fabricated approvals were written to the target repository.
6. **Report Remaining Decisions**: Provide a concise summary in conversation of files generated, files preserved, and open questions awaiting developer decision.
7. **Format and Ownership**: Check new and merged destinations against applicable recipe headings/order, content boundaries, and concrete unknowns. Count final AGENTS physical lines and verify its required task routing against the AGENTS recipe. For outlines or partial documents, verify top-of-file notices, section-level filling actions, and incomplete labels on inbound indexes/routes; report them as unfinished, never as a completed knowledge base. Confirm architecture owns the repository map, development owns invocation procedures, and entrypoints/spec indexes route without duplicating technical manuals.
