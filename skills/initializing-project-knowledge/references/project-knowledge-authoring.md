# Project Knowledge Authoring Guide

Use the recipe for each document being written or audited. The [Project Knowledge Standard](project-knowledge-standard.md) owns layout, evidence, approval, legacy handling, and feature-spec schema. This guide owns the other document outlines and how to write them.

## Applying a Recipe

Use the exact English headings and relative order under **Outline and Writing Instructions**; use the project's own title and content. Additional project-specific subsections belong under the relevant standard heading. Recipe labels are authoring instructions, not headings to copy into output.

`Include when: <condition>` marks conditional sections in plain prose outside the output heading. Other listed sections are required when their document is created. Omit irrelevant conditional sections; for a required but unresolved subject, name the specific unknown and decision needed. A concrete unknown is not an invitation to create empty scaffolds. Create a document only when evidence or explicit decisions support useful content. The standard's feature-spec non-applicability rules remain authoritative.

Inspect evidence permitted by the standard, including its legacy-source gate. Distinguish implemented behavior, proposed choices, and approved intent. Illustrative examples below are not project facts, default architectures, or reusable business rules.

Keep one content owner. Tooling owns command definitions and versions; documentation explains non-obvious use, sequencing, rationale, and hazards. Generated project documents must resolve local links inside that project, not depend on this guide, installed skills, or the skill repository. External product/API references are allowed. Transfer necessary spec-format and workflow guidance into the project's own spec index/workflow rather than linking back to skill references.

## README.md

**Purpose:** Explain what the repository is for and where a developer starts.

**Read When:** Evaluating the project or onboarding to it.

**Evidence:** Confirmed purpose, actual entrypoints and capabilities, intended audience, and existing documentation destinations.

**Outline and Writing Instructions:**
1. `## Purpose`: State the problem and scope in project terms.
2. `## Audience`: Identify the actual users or maintainers; record uncertainty if not established.
3. `## Capabilities`: Summarize evidenced capabilities; label planned behavior as planned.
4. `## Getting Started`: Link to local development instructions, with any supported prerequisite context.
5. `## Documentation`: Link to the docs index, agent instructions, and architecture's repository map when those exist.

**Content Boundaries:** Setup procedures belong in development; business rules in specs; detailed structure in architecture. Add links only to actual destinations, not a future scaffold.

**Example:** Illustrative navigation: `For local setup, see [Development](docs/development.md).` Use it only after that file exists in the target.

**Done When:** A newcomer can identify purpose, audience, current versus planned capabilities, and the next reading step; destinations resolve and setup/map content has one owner.

## AGENTS.md

**Purpose:** Give every coding agent mandatory cross-task instructions and dependable task routing.

**Read When:** Beginning work in the repository; follow applicable routes before changing affected behavior or modules.

**Evidence:** Repository scope, actual standards/spec destinations, approved stop rules, non-obvious project-wide hazards, and supported verification procedures.

**Outline and Writing Instructions:**
1. `## Scope`: Define the instruction scope and minimum context needed to recognize the project. State any actual narrower instruction scopes without creating a mandatory nested-instruction tree.
2. `## Task Routing`: Pair each task condition with a relative destination, using section anchors when useful. Cover module placement, implementation, test authoring, execution, and business behavior when applicable. Add UI and persistence routes only for relevant projects. Read all applicable routes; a single-spec limit is not a general rule.
3. `## Approval Boundaries`: State actionable stop conditions and the decision needed, linking to the project's workflow for detail. A conflict between approved spec and observed behavior requires a developer decision, not unilateral selection of a winner.
4. `## Completion`: Identify required observed verification, affected documentation reconciliation, and remaining-decision reporting. Link to procedures instead of copying command catalogs.

**Content Boundaries:** Keep root instructions compact by scope, not an arbitrary line limit. Architecture owns structure, standards own implementation/test guidance, specs own business rules, and the workflow owns detailed approval stages. Keep a guardrail with its technical topic unless it genuinely applies across tasks. CLAUDE points here; rules are not copied back into it.

**Example:** Illustrative routing; retain only applicable rows with real target files:

```markdown
## Task Routing

- Module placement or dependency changes: read [Architecture](docs/architecture.md#repository-map).
- Implementation changes: read [Coding Standards](docs/standards/coding.md).
- Test authoring: read [Testing Standards](docs/standards/testing.md).
- Running or troubleshooting: read [Development](docs/development.md).
- Business behavior changes: select all affected specs in the [Spec Index](docs/specs/README.md), then follow [Spec Changes](docs/workflows/spec-changes.md).
```

**Done When:** For every applicable task branch, a reader can reach the authoritative material before acting; conditions distinguish actual tasks; stop rules say what needs a decision; no manual, schema, full project tree, or duplicated business rules have accumulated here. Trace actual links, including CLAUDE to AGENTS.

## CLAUDE.md

**Purpose:** Enter the same shared instructions from Claude runtimes.

**Read When:** Claude discovers its root instruction file.

**Evidence:** An existing root AGENTS file.

**Outline and Writing Instructions:** Use a project-specific title and one short instruction to read and follow `[AGENTS.md](./AGENTS.md)`. No additional sections or runtime-specific include syntax.

**Content Boundaries:** AGENTS owns all rules. Always create this entrypoint when generating the standard knowledge structure.

**Example:** Illustrative complete file, replacing the title with the project's own name:

```markdown
# Example Project Agent Instructions

Read and follow [AGENTS.md](./AGENTS.md) before working in this repository.
```

**Done When:** The relative link reaches AGENTS and every instruction is owned there rather than duplicated here.

## docs/README.md

**Purpose:** Help humans and agents discover the right documentation for a task.

**Read When:** Onboarding, locating context, or deciding which document answers a question.

**Evidence:** The actual document inventory, their content ownership, and supported task paths.

**Outline and Writing Instructions:**
1. `## Reading Paths`: Describe starting paths for onboarding, architecture, implementation, testing, business behavior, and other real branches. Prefer task conditions over a blanket read-everything order.
2. `## Document Index`: List existing documents with scope and links; group by meaningful category. Point feature selection to the spec index instead of duplicating every feature row.

**Content Boundaries:** Navigation and scope only; mandatory agent rules stay in AGENTS, setup in development, and feature routing detail in the spec index.

**Example:** Illustrative path: `Changing module boundaries? Start with [Architecture](architecture.md#boundaries-and-dependencies).`

**Done When:** Every active document is discoverable directly or through an indexed sub-index; reading paths reach actual content without restating its rules.

## docs/project.md

**Purpose:** Explain business context and vocabulary shared across features.

**Read When:** Understanding actors, scope, domain boundaries, or unfamiliar domain terms.

**Evidence:** Developer answers, domain concepts in implementation/tests, approved specs, manifests/config, and permitted legacy sources. Label code-inferred context accordingly.

**Outline and Writing Instructions:**
1. `## Purpose and Scope`: Define the business problem and explicit exclusions.
2. `## Actors`: Describe established personas and responsibilities; distinguish users from external systems.
3. `## Domain Boundaries`: Identify actual domains and their responsibilities without prescribing a domain-driven architecture.
4. `## Glossary`: Define shared terms; preserve identifiers and resolve uncertain translations with the developer.
5. `## Technology References`: Link to real manifests/config and explain non-obvious choices; name undecided stack decisions when appropriate.

**Content Boundaries:** Feature-specific terms refine rather than redefine this glossary. Version lists belong to tooling, technical boundaries to architecture, and detailed rules to specs.

**Example:** Illustrative glossary distinction: explain whether a project's `Account` means a customer organization or a login identity, based on its own usage rather than a generic definition.

**Done When:** Actors, scope, and shared terms agree with supported evidence; unresolved meanings are visible; dependency versions and feature rules are not copied here.

## docs/architecture.md

**Purpose:** Explain system composition, where changes belong, and the boundaries they must respect.

**Read When:** Placing code, changing dependencies or runtime topology, or following a cross-module flow.

**Evidence:** Actual entrypoints, import/dependency boundaries, configuration, integrations, representative call paths, and explicit architecture decisions. For a new project, distinguish agreed design from implemented state.

**Outline and Writing Instructions:**
1. `## System Context`: State system responsibility and external actors/systems with real boundaries.
2. `## Runtime Components`: Describe actual processes and how they communicate. Include when: runtime behavior exists or runtime components have been explicitly decided. Label planned components as planned.
3. `## Repository Map`: Own the canonical project structure. Use a selective annotated tree or responsibility table, not both for the same information. Explain major directories, entrypoints, where common changes belong, and any generated code's source and regeneration link. For an empty project, say that implementation layout is undecided; do not invent implemented directories.
4. `## Boundaries and Dependencies`: Explain allowed/evidenced dependency directions, ownership, and non-obvious constraints. Separate observations from approved architectural requirements.
5. `## Key Flows`: Describe representative cross-component flows from actual code or approved design. State specific discovery gaps when no flow is established.
6. `## Rationale`: Explain reasons backed by decisions, distinguishing unknown historical reasons from recommendations. Link durable later decisions to ADRs when present.

**Content Boundaries:** Repository Map owns semantic project structure; README and AGENTS link here. Keep feature code/test mappings in their specs and physical schema detail in data-model/schema sources. Repository Map links to adjacent dependency rules rather than repeating them.

**Example:** Illustrative responsibility table, only if these paths and roles actually exist:

| Path | Responsibility | Change placement |
|---|---|---|
| `src/billing/` | Billing policy and application operations | Billing behavior; consult the billing spec first |
| `src/adapters/` | External service boundaries | Provider-specific translation, not billing policy |

**Done When:** Each significant module has an evidenced role; a reader can place a representative change and follow dependency boundaries; generated artifacts are distinguishable; no unexplained full directory dump or second authoritative tree exists elsewhere.

## docs/data-model.md

**Purpose:** Explain persistent entity relationships and their physical sources.

**Read When:** Changing stored data, constraints, relationships, or persistence ownership.

**Evidence:** Actual schema/migrations/models, storage configuration, feature data access, and explicit decisions. Create only when persistent data exists; an undecided future store is not evidence of physical tables.

**Outline and Writing Instructions:**
1. `## Storage Overview`: Identify evidenced stores, their roles, and source definitions.
2. `## Entities and Relationships`: Describe shared entities and cardinalities. Use domain views when large; feature views must agree with this shared model.
3. `## Constraints and Ownership`: Separate enforced keys/nullability/uniqueness from application-enforced or intended business invariants. Explain ownership and sensitive lifecycle boundaries only when supported.
4. `## Schema References`: Link actual physical definitions/migrations; identify whether a model is authoritative or generated.

**Content Boundaries:** Explain relationships instead of copying a complete DDL catalog. Feature specs own feature persistence flows; schemas own physical definitions. Never infer distributed atomicity from a transaction-related identifier.

**Example:** Illustrative distinction: `Uniqueness is checked in application code; no matching database constraint was found in the inspected migrations.` Use only after inspection supports it.

**Done When:** Diagram relationships and claims match cited schema sources; constraint enforcement layers are clear; all feature ERD views agree; missing physical definitions remain explicit.

## docs/development.md

**Purpose:** Make supported local setup, execution, and verification procedures reproducible.

**Read When:** Preparing an environment, running the project, checking a change, or troubleshooting.

**Evidence:** Manifests, scripts/Makefiles, config, example environment files, supported runtime help, and observed execution. Never expose secret values; distinguish inspected commands from commands actually run.

**Outline and Writing Instructions:**
1. `## Prerequisites`: Link version/config sources; explain prerequisites the tooling does not make obvious. Name unresolved requirements for uninitialized projects.
2. `## Local Setup`: Give supported sequencing and non-obvious setup decisions; reference command definitions rather than invent commands for a future stack.
3. `## Environment`: Explain required variable names, purpose, safe sources, and service dependencies. Include when: environment configuration exists or is explicitly specified. Secret values stay outside documentation.
4. `## Running the Project`: Explain actual invocation and readiness observations. Include when: a runnable surface exists or its invocation is explicitly decided. Do not present planned commands as verified.
5. `## Verification`: Explain supported lint/test/build/smoke invocations and prerequisites, linking tooling definitions. Note relevant backend/service limitations instead of claiming an in-memory substitute proves production behavior.
6. `## Troubleshooting`: Record observed or explicitly established symptoms, causes, and remedies. Include when: supported troubleshooting knowledge exists.

**Content Boundaries:** This file owns documented command use and sequencing. Testing/coding standards link here for execution and own methodology/rules instead. Tooling remains authoritative for command definitions; avoid copying its full option catalog.

**Example:** Illustrative precision: `The unit suite needs no database service; PostgreSQL integration verification is separate.` Only state this distinction when the project's tooling supports it.

**Done When:** Instructions resolve to actual tooling or explicit decisions, prerequisites precede use, environment names expose no secrets, and any observed execution is distinguished from unrun guidance. No speculative commands fill missing setup.

## docs/standards/coding.md

**Purpose:** Explain implementation conventions that matter beyond what configuration already enforces.

**Read When:** Writing/reviewing implementation or choosing among existing patterns.

**Evidence:** Linter/formatter config, representative production code, boundary/error conventions, tests, and explicit developer decisions. A small fixture is not enough to infer a universal style guide.

**Outline and Writing Instructions:**
1. `## Implementation Patterns`: Describe evidenced patterns and their applicability, including rationale/gotchas. Inferred patterns remain observations or proposals, not invented mandates.
2. `## Naming and Error Handling`: Explain project-specific naming/error semantics and their sources. Record uncertainty instead of generic rules where no convention is established.
3. `## Boundary Conventions`: Describe supported module/API/persistence boundaries and link architecture for the overall dependency policy.
4. `## Examples`: Link representative real code, naming the behavior to study and its applicability. For an unimplemented project, explicitly say examples are not yet available.
5. `## Exceptions and Proposals`: Record supported exceptions or unapproved proposed conventions. Include when: exceptions/proposals exist, clearly distinguished from mandatory rules.

**Content Boundaries:** Reference config rather than transcribing formatter settings. Keep business requirements in specs, dependency policy in architecture, and test methodology in testing standards. Prefer links to maintained implementation over large copied boilerplate.

**Example:** Illustrative rule shape: `For provider failures, follow the existing error translation in <actual implementation link>; retain the provider code for diagnosis.` The target and rule require project evidence.

**Done When:** Each asserted convention has evidence or explicit approval, examples exist or their absence is stated, proposals are labelled, and framework-specific advice is limited to this project's actual stack.

## docs/standards/testing.md

**Purpose:** Explain what to test, at which boundary, and how to isolate meaningful behavior.

**Read When:** Selecting coverage, writing tests, or reviewing test adequacy.

**Evidence:** Actual tests and runner/configuration, fixture patterns, meaningful failure boundaries, and explicit quality decisions. No existing tests is a fact to record, not permission to invent an established strategy.

**Outline and Writing Instructions:**
1. `## Test Strategy`: Identify actual layers and their responsibilities. Distinguish observed coverage from approved plans; do not assume unit/integration/e2e all exist.
2. `## Isolation and Fixtures`: Explain existing state/service isolation and fixtures, including limits of substitutes. State missing conventions where necessary.
3. `## Assertions and Failure Cases`: Describe observable behavior, boundary cases, errors, and invariants using real examples; explain which gaps remain untested.
4. `## Execution`: Link to development's Verification section for commands and prerequisites.

**Content Boundaries:** Strategy and authoring live here, invocation procedures in development, feature acceptance criteria in specs. Keep code/test mappings with their owning features.

**Example:** Illustrative distinction: testing a calculation return value does not prove its caller committed a persisted state transition; document the boundary actually exercised.

**Done When:** A developer can select a test boundary, understand fixture limits, and locate invocation instructions; no unobserved coverage or execution success is claimed.

## docs/standards/ui.md

**Purpose:** Define shared UI implementation conventions without confusing them with feature behavior.

**Read When:** Building/reviewing components, styles, interaction states, or accessibility behavior. Create only for a project with a UI or an explicitly agreed UI foundation.

**Evidence:** Existing components/styles/tokens, tests, accessibility checks, and explicitly agreed component contracts. Screen mockups are not a prerequisite.

**Outline and Writing Instructions:**
1. `## Component Ownership`: Define shared versus feature-specific components and agreed APIs using the project's vocabulary.
2. `## Styling and Tokens`: Describe the actual system. Include only evidenced/chosen tokens and defaults; name unresolved styling decisions instead of supplying generic breakpoints.
3. `## Interaction States`: Describe evidenced or agreed loading, disabled, error, and other applicable states, without assuming every component implements each one.
4. `## Accessibility`: Describe implemented or agreed requirements; record gaps and proposals separately from current guarantees.
5. `## Examples`: Link actual components or quote an explicitly agreed unimplemented contract, labelled as such. Record unavailable implementation honestly.

**Content Boundaries:** Shared component/tokens belong here, feature journeys in specs, command use in development. Project purpose or responsive aspirations do not authorize unchosen prop defaults, thresholds, or token values.

**Example:** Illustrative contract distinction: `Agreed Button states: idle, loading, disabled. Component implementation is not yet available.` Only use states actually agreed for that project.

**Done When:** Shared standards and feature behavior have separate owners, actual versus planned requirements are explicit, examples are grounded, and no mandatory mockups or invented UI defaults were introduced.

## docs/workflows/spec-changes.md

**Purpose:** Define how this project discovers, approves, implements, and verifies spec changes.

**Read When:** Proposing or changing feature behavior, reconciling discrepancies, or checking approval before implementation.

**Evidence:** The standard's approval/evidence rules, explicit project decisions, and actual implementation/verification procedures. Write a self-contained project workflow rather than linking to installed skill references.

**Outline and Writing Instructions:**
1. `## When to Use`: Define behavior-changing triggers and distinguish behavior-preserving maintenance.
2. `## Discovery and Conflicts`: Input: affected request/spec/code/tests. Action: gather permitted evidence and present conflicting sources, impact, open questions, and the required decision. Done: affected scope and unresolved conflicts are explicit.
3. `## Drafting`: Input: evidence and decisions. Action: revise affected rules/flows/criteria in draft form using the local format. Done: every in-scope behavioral uncertainty is recorded, and unaffected behavior remains unchanged.
4. `## Approval`: Input: complete draft and material questions. Action: request explicit contextual developer consent. Done: all in-scope rules/flows/criteria are covered by consent; excluded future topics do not block it.
5. `## Implementation`: Input: approved behavior and authorized scope. Action: implement only that scope and reconcile real code/test mappings. Done: implementation and affected documentation agree or remaining gaps are reported.
6. `## Verification`: Input: observable acceptance criteria. Action: run supported checks and report actual outcomes. Done: evidence supports the result; unexecuted criteria are not marked as passed.

**Content Boundaries:** The workflow owns procedural detail; AGENTS carries concise cross-task stop conditions. Feature specs own behavior and evidence mapping, not per-change approval logs. Preserve the standard's ban on change/proposal archives.

**Example:** Illustrative conflict presentation: quote the approved rule and observed implementation with source locations, explain the known impact, then ask which behavior is intended before modifying either.

**Done When:** Every stage has a checkable input/action/exit, scope and approval gates are preserved, and a reader can follow the workflow entirely within the generated project.

## docs/specs/README.md

**Purpose:** Select all relevant feature specs and explain the local spec format/lifecycle.

**Read When:** Locating business behavior, planning a cross-feature change, or authoring a spec.

**Evidence:** Existing specs, their actual scope and related specs, real code mappings, and the standard's feature schema.

**Outline and Writing Instructions:**
1. `## Selecting Specifications`: Explain discriminating task conditions and how to combine overlapping domains. Do not impose a universal one-spec-only rule.
2. `## Domain and Feature Index`: Use a task-oriented table of domain/feature, scope or trigger, and spec link. Add key model/code mapping only where it improves selection and can be maintained; detailed mappings remain in each spec.
3. `## Format and Lifecycle`: Explain the required feature format in project-local terms, including status semantics and links to the project's spec-change workflow. Transfer the standard's necessary schema guidance here without a dependency on the skill repository.

**Content Boundaries:** Feature rules live in the features; index rows provide only enough distinction to choose them. Workflow steps live in the workflow; shared glossary in project.md.

**Example:** Illustrative scope distinctions: catalog pricing selects master/base-price rules; billing settings selects configurable rates/cutoffs; checkout selects calculation/application of those inputs. A change spanning these boundaries reads all affected specs, if such domains actually exist.

**Done When:** Each spec is discoverable, overlapping terms have distinct triggers, local format/lifecycle guidance is sufficient without installed skills, and every index link resolves.

## Feature Specifications

**Purpose:** State one feature's intended behavior precisely, with traceable evidence and observable criteria.

**Read When:** Changing, reviewing, implementing, or verifying that feature and its affected dependencies.

**Evidence:** Apply the standard's evidence hierarchy and approval gates. Distinguish approved intent, current code behavior, test expectations, and physical schema constraints.

**Outline and Writing Instructions:** Follow the authoritative [Feature Spec Format](project-knowledge-standard.md#feature-spec-format), including its headings, order, metadata, and non-applicability instructions. Build scope and glossary before stable numbered rules; trace rules through data access, failure consistency, acceptance criteria, and actual implementation/test mappings. Status describes approval, not completion. Keep material in-scope questions explicit; do not block approval on excluded future topics.

**Content Boundaries:** Shared entity relationships must agree with data-model; technical conventions link to standards. Record relevant current implementation gaps separately within Implementation & Test Mapping, with sources, rather than rewriting approved behavior to match a bug. Project-specific subsections may clarify existing sections without replacing the schema.

**Example:** Illustrative distinction: `Observed: evaluation returns True. Unknown: whether its caller persists cancellation.` A return value alone does not establish a persisted side effect.

**Done When:** Every rule is supported and approval is honest; flows separate reads, validation, transitions, and writes; failure claims match evidence; criteria are observable and not fabricated execution logs; mapped paths exist or explicitly say Not yet available.

## Architecture Decision Records

**Purpose:** Preserve why a durable technical decision was made and its consequences.

**Read When:** Proposing or revisiting a durable architecture choice. Create only when such a decision warrants an ADR; initial architecture rationale belongs in architecture.md.

**Evidence:** Explicit decision context, evaluated alternatives, developer consent, and affected architecture. Use `docs/decisions/NNNN-short-title.md`: choose the next unused sequential positive number from existing ADRs, starting at `0001`; recheck availability before writing and preserve existing numbering. No numbering service is needed.

**Outline and Writing Instructions:**
1. `## Status`: proposed, accepted, or superseded. Accepted requires explicit approval, not implementation presence.
2. `## Context`: State the concrete problem, constraints, and forces behind the choice.
3. `## Decision`: State the chosen or proposed technical approach and its scope.
4. `## Alternatives`: Record genuine considered alternatives and relevant tradeoffs, not fabricated deliberation.
5. `## Consequences`: Describe evidenced/expected benefits, costs, and follow-on obligations; distinguish predictions from observations.
6. `## Related Decisions`: Link predecessors/successors and affected architecture. Include when: related decisions exist. Superseded records must link to their replacement.

**Content Boundaries:** The ADR owns historical rationale, architecture owns the current system description, and specs own business behavior. Do not use ADRs as per-change approval logs or invent prior decisions.

**Example:** Illustrative status handling: an implemented library choice may still be a proposed ADR when the rationale and explicit adoption decision are unconfirmed.

**Done When:** The record explains the actual decision and tradeoffs, approval/status are grounded, numbering does not collide, and supersession links resolve where applicable.
