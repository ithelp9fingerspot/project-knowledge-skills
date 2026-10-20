# Project Knowledge Standard

Authoritative specification for repository documentation structure, document responsibilities, feature specification format, evidence requirements, approval boundaries, and legacy documentation handling.

---

## Document Layout

Every documented repository uses a standardized, modular documentation tree. Files are created only when supported by evidence or explicit decisions; never generate empty scaffolds.

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
- `docs/decisions/`: Created only when a durable technical architectural decision warrants an Architecture Decision Record (ADR). Initial architectural rationale belongs in `docs/architecture.md`.
- `docs/data-model.md`: Created only when the project stores persistent data.
- `docs/standards/ui.md`: Created only when the project contains a user interface.
- Do not create a `changes/` directory, proposal archive, approval log, or per-change documentation artifacts.

---

## Document Responsibilities

Each document has a distinct scope and purpose. Avoid duplicating information across documents; link to the authoritative source instead.

### Root Entrypoints
- `README.md`: Concise introduction to the repository, its purpose, target audience, and direct links to setup instructions (`docs/development.md`) and project documentation (`docs/README.md`).
- `AGENTS.md`: Mandatory instructions for AI coding agents. Functions as a concise navigation map, setting out contextual reading paths, stop/confirmation rules, and links to technical standards and spec workflows. Keep it compact; do not dump full manuals into this file.
- `CLAUDE.md`: Minimal entrypoint directing Claude runtimes to read `AGENTS.md`. Contains a standard relative Markdown link (`[AGENTS.md](./AGENTS.md)`) and instructions to follow the rules in `AGENTS.md`. Do not duplicate rules from `AGENTS.md`.

### Project & Architecture
- `docs/README.md`: Task-oriented documentation index and reading guide for human developers and agents navigating the knowledge base.
- `docs/project.md`: High-level business purpose, user personas, domain glossary, and technology stack overview. Links directly to package manifests and configuration files rather than manually copying dependency versions.
- `docs/architecture.md`: System design, module responsibilities, architectural boundaries, dependency flows, and architectural rationale.
- `docs/data-model.md`: Repository-wide entity-relationship overview, core entity definitions, storage engines, and links to physical schemas or migrations. Break large models into domain diagrams.

### Development & Standards
- `docs/development.md`: Prerequisites, local setup, execution commands, environment variable names (never secret values), test execution, and troubleshooting. Other documents link here instead of repeating commands.
- `docs/standards/coding.md`: Language-specific and framework-specific implementation patterns, naming conventions, and error-handling conventions grounded in repository configuration and linters. Do not invent generic conventions (e.g. PEP 8, generic style guides) from small fixtures; label unconfigured patterns as proposals until approved.
- `docs/standards/testing.md`: Testing strategy, test layers (unit, integration, e2e), fixture conventions, assertion styles, and test execution commands.
- `docs/standards/ui.md`: Component conventions, styling/theming systems, layout patterns, interaction states, accessibility requirements, and code patterns. Does not demand mandatory screen mockups.

### Workflows & Specifications
- `docs/workflows/spec-changes.md`: Lifecycle procedure for proposing, approving, implementing, and verifying feature specification changes.
- `docs/specs/README.md`: Index of feature specifications grouped by domain, explaining the feature specification format and lifecycle.

---

## Feature Spec Format

Feature specifications live under `docs/specs/<domain>/<feature>.md`. Every feature spec adheres to a consistent structure. If a section does not apply (e.g. no persistent data), state that concisely rather than inventing details.

```markdown
# [Feature Name]

## Status & Metadata
- **Domain**: [Domain name]
- **Status**: draft | approved
- **Last Updated**: YYYY-MM-DD
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
- Ground rules strictly in observable code/schema; do not strengthen terminology beyond evidence (e.g. do not turn `GRACE_DAYS = 7` into "calendar days" or "business days" without explicit backing).
- Distinguish return values from side effects (e.g. an evaluation returning `True` does not mean an entity was cancelled or persistence updated).
- Do not assert unevidenced architectural guarantees (e.g. thread-safety, distributed atomicity) from identifiers alone.
## Data Model & Persistence
ERD view relevant to this feature (view of the shared data model, not a disconnected schema).
- Entities, table roles, key columns, and constraints.
- (If no persistent data, state: "No persistent data.")

## Flows & Data Access
Step-by-step user and system flows:
1. Step description: data read, validation, state transition, and data written.
2. Step description...

## Failure Modes & Consistency
- Domain validation errors, boundary cases, and partial-failure consistency invariants.
- Do NOT elevate low-level language type errors or theoretical constant-type mutations (e.g. "raises `TypeError` if constant is non-numeric") into approved business failure rules.
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
- Unresolved questions requiring developer decision. Any open question prevents `approved` status.
```

### Specification Status Invariants
- `draft`: Specification under discovery, review, or containing open questions. Inferred rules from code or tests must remain `draft` until explicitly approved. Implementation presence in code is not specification approval.
- `approved`: Explicit developer consent has been obtained for all business rules, flows, and criteria.
- Status describes *specification approval*, not implementation completion.
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
  - Existing files are preserved and updated incrementally.
  - Unique operational runbooks, compliance records, and notes are retained.
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
- Do not require proprietary tools, MCP servers, runtime-specific hooks, or custom configuration formats.
- `CLAUDE.md` must be a plain Markdown file with standard relative links, avoiding proprietary syntax.

---

## Verification

Before declaring documentation generation complete, verify:
1. **Link Integrity**: All relative links within `README.md`, `AGENTS.md`, `CLAUDE.md`, and `docs/` resolve to existing files.
2. **Reading Route**: Verify that starting at `CLAUDE.md` leads to `AGENTS.md`, and `AGENTS.md` correctly directs navigation into `docs/`.
3. **Data Model Consistency**: Ensure feature ERDs reflect the shared application data model in `docs/data-model.md` without contradictory relationships.
4. **Draft Status Integrity**: Confirm all unapproved or inferred business rules remain labeled as `draft`.
5. **No Invented Artifacts**: Verify no temporary discovery files, `changes/` folders, or fabricated approvals were written to the target repository.
6. **Report Remaining Decisions**: Provide a concise summary in conversation of files generated, files preserved, and open questions awaiting developer decision.
