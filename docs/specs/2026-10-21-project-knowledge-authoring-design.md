# Project Knowledge Authoring Design

## Intent and Approval State

Define a consistent format for project documentation while deriving all substantive content from the project being documented. This design is awaiting approval together with its implementation plan; it does not authorize implementing the guide yet.

User decisions:
- Standardize document format; content always adapts to the project.
- Provide detailed guidance for writing every standard document, especially `AGENTS.md` and the project structure map.
- Use scout agents for project exploration.
- Keep `AGENTS.md` authoritative across general coding agents; always generate a thin `CLAUDE.md` entrypoint linking to it.

## Goals

- Give each document an ordered outline, explicit content ownership, evidence inputs, writing instructions, and checkable completion criteria.
- Make task-conditioned navigation reliable without loading complete manuals into entrypoints.
- Give project structure one authoritative home in `docs/architecture.md`.
- Distribute the guide with every standalone consumer skill that needs to write or audit these documents.

## Non-Goals

- Change the Fingerspot backend or copy its Go, GORM, Atlas, worker, or testing conventions into generic guidance.
- Prescribe a stack, architecture, business rules, test layers, or persistence system for all projects.
- Change evidence, approval, legacy source/write-mode, English-language, or portability policies.
- Introduce another skill, documentation generator, approval archive, or mandatory nested `AGENTS.md` tree.

## Packaging and Ownership

Keep `shared/project-knowledge-standard.md` as the normative source for layout, document responsibilities, feature spec format, evidence, approval, and verification. Add `shared/project-knowledge-authoring.md` as an on-demand reference for how to write and assess each document.

The standard owns the document-format policy and points to the authoring guide for ordered outlines. The guide owns those outlines and writing recipes. Existing feature-spec headings, fields, and approval invariants remain authoritative in the standard; the guide links to them instead of copying the template. A future feature-spec heading change is made only in the standard; its authoring recipe changes only if the writing instructions change.

Extend `scripts/sync-references.py`, preserving `sync_references(root: Path, check: bool) -> list[Path]` and its CLI flags and exit codes, to copy both canonical references into each of these standalone packages:
- `skills/initializing-project-knowledge/references/`
- `skills/documenting-existing-projects/references/`
- `skills/working-with-project-specs/references/`
- `skills/auditing-project-knowledge/references/`

Bundled references link locally to each other. Consumer skills point to the guide only at the writing or auditing branch, and direct the reader to the recipes for affected documents. A task changing one spec need not read every authoring recipe. Canonical files remain the only manually edited reference sources.

Every generated project document must be self-contained: local documentation links resolve inside that project. Generated output must not depend on this skills repository, an installed skill path, or bundled skill references. Normal external product or API documentation links remain permitted.

## Format Contract

For each applicable document, use the exact English section names and relative order defined below. The project title and feature name remain project-specific. Recipe headings describe authoring instructions and are not inserted into generated documents.

Required sections contain supported project-specific information. Optional sections and files appear only when relevant and supported by evidence or explicit decisions. Use a short, specific unknown or unresolved decision where a required subject cannot be established; do not fill it with generic advice or invented facts. Initializing a project may record an explicitly undecided architecture rather than imply implemented modules. The existing feature-spec policy for non-applicable sections remains unchanged.

Implementation call: use semantic requirements rather than fixed document lengths, tree depths, or counts of examples. Additional project-specific subsections may follow the relevant standard section without replacing or reordering standard sections. Project-specific supplementary documents can be linked where they serve a real branch.

## Authoring Recipe Format

Each file recipe uses this sequence:
1. **Purpose**: questions this document must answer.
2. **Read When**: task conditions that should route a reader here.
3. **Evidence**: permitted source types and what to establish from them; legacy-source permission follows the standard.
4. **Outline and Writing Instructions**: ordered destination headings, what belongs under each, and applicability conditions.
5. **Content Boundaries**: authoritative ownership and where to link instead of duplicating content.
6. **Example**: a compact, explicitly illustrative fragment showing a non-obvious writing choice; examples are not project facts or reusable business requirements.
7. **Done When**: observable checks covering the recipe's obligations.

Use concise examples where they clarify routing, structure annotation, or separation of intended and observed behavior. A correct minimal `CLAUDE.md` is an example in its own right. For feature specs, link to the standard's template and use the recipe to explain evidence and writing decisions.

## Ordered Document Outlines

| Document | Ordered sections | Applicability and boundary |
|---|---|---|
| `README.md` | `Purpose`, `Audience`, `Capabilities`, `Getting Started`, `Documentation` | Describe actual or explicitly planned capabilities accurately. Getting Started links to development instructions rather than copying commands. |
| `AGENTS.md` | `Scope`, `Task Routing`, `Approval Boundaries`, `Completion` | Only instructions that apply across tasks and conditional pointers. Repository maps, implementation examples, and business rules stay at their authoritative destinations. |
| `CLAUDE.md` | Project-specific title followed by a short instruction to read and follow `[AGENTS.md](./AGENTS.md)` | No additional rule sections. Plain Markdown, no runtime-specific include syntax. |
| `docs/README.md` | `Reading Paths`, `Document Index` | Human and agent navigation, with task conditions and document scope; not a second copy of mandatory agent rules. |
| `docs/project.md` | `Purpose and Scope`, `Actors`, `Domain Boundaries`, `Glossary`, `Technology References` | Business overview and shared terms; link to tooling/config rather than copying versions. |
| `docs/architecture.md` | `System Context`, `Runtime Components`, `Repository Map`, `Boundaries and Dependencies`, `Key Flows`, `Rationale` | Implementation uncertainty is explicit. Runtime Components applies only when there is runtime behavior; other required subjects can record concrete discovery gaps. |
| `docs/data-model.md` | `Storage Overview`, `Entities and Relationships`, `Constraints and Ownership`, `Schema References` | File only when persistent data exists. Distinguish schema-enforced constraints from business intent. |
| `docs/development.md` | `Prerequisites`, `Local Setup`, `Environment`, `Running the Project`, `Verification`, `Troubleshooting` | Runtime/environment sections only when relevant. Owns documented invocation procedures, links to command definitions, and non-obvious sequencing or gotchas. |
| `docs/standards/coding.md` | `Implementation Patterns`, `Naming and Error Handling`, `Boundary Conventions`, `Examples`, `Exceptions and Proposals` | Ground patterns in actual config, code, or explicit decisions. Examples link to representative implementation. Include exceptions/proposals only when present. |
| `docs/standards/testing.md` | `Test Strategy`, `Isolation and Fixtures`, `Assertions and Failure Cases`, `Execution` | Document actual layers; do not invent a complete pyramid. Execution links to development instructions instead of copying commands. |
| `docs/standards/ui.md` | `Component Ownership`, `Styling and Tokens`, `Interaction States`, `Accessibility`, `Examples` | File only when a UI exists. Tokens or component details only if evidenced or explicitly chosen. |
| `docs/workflows/spec-changes.md` | `When to Use`, `Discovery and Conflicts`, `Drafting`, `Approval`, `Implementation`, `Verification` | Each stage identifies its input, action, and completion condition. Preserve existing explicit-approval requirements. |
| `docs/specs/README.md` | `Selecting Specifications`, `Domain and Feature Index`, `Format and Lifecycle` | Routing distinguishes overlapping domains; links to the repository's spec-change workflow. Generated projects must be self-contained, not link to this skill repository. |
| Feature spec | Existing headings and order from the standard | Preserve metadata, stable rule IDs, status semantics, acceptance criteria, and code/test mapping requirements. |
| ADR under `docs/decisions/` | `Status`, `Context`, `Decision`, `Alternatives`, `Consequences`, `Related Decisions` | Only for a durable technical decision. Implementation call: use `NNNN-short-title.md`, selecting the next unused positive sequential number from existing ADRs, beginning with `0001`; recheck availability before writing and preserve existing numbering. No numbering service or new concurrency mechanism. Status is proposed, accepted, or superseded. Explicit approval is required for accepted; include supersession links where applicable. Initial architecture rationale remains in architecture.md. |

The guide marks conditional sections in plain Markdown prose using `Include when: <condition>` in the recipe, outside the destination heading. This is an agent/human writing contract, not machine-readable metadata; no parser or conditional-section synchronization tooling is introduced. Required headings are not a demand to invent features, infrastructure, or conventions.

## Repository Map

`docs/architecture.md#repository-map` is the canonical home for project structure. Use a selective annotated tree or a responsibility table, choosing the representation that communicates ownership with least duplication. The section explains:
- Entrypoints and major module responsibilities.
- Where common change types belong.
- Dependency direction and architectural boundaries, linked to the adjacent boundaries section rather than repeated.
- Relevant generated artifacts, their source, and a link to regeneration instructions.

The map is a semantic explanation, not a complete listing or a cache of filenames. README and AGENTS route to it. Feature specs retain only their feature-specific implementation/test mappings.

## Task Routing

Pointers state both their destination and the task condition. The root AGENTS routes module placement to architecture, implementation to coding standards, test authoring to testing standards, execution to development, and business behavior to the spec index plus change workflow. UI and persistence routes appear only for applicable projects.

The spec index explains how to distinguish overlapping domains, such as catalog pricing versus checkout calculation. Read every affected specification, rather than applying a universal single-spec limit. A task may require several routes; satisfying one does not replace another applicable route.

`docs/README.md` serves human discovery and document scope; AGENTS owns mandatory agent behavior. The two entrypoints link rather than repeat rule text.

## Evidence and Command Ownership

Apply the existing evidence and legacy-source gates before using project material. Examples in the generic guide are labelled illustrative. A convention inferred from code is not elevated into an approved rule. An implementation gap is described separately from intended behavior, with sources and unresolved questions; it does not justify silently changing either code or spec.

Tooling remains authoritative for command definitions. Development documentation records how to use those commands, necessary setup, ordering, and troubleshooting. Testing standards explain which behavior to test and how, then link to development for invocation. Coding standards reference lint rules/config without reproducing command catalogs.

## Verification and Acceptance

- Every document in the standard has an applicable recipe, including thin CLAUDE and conditional ADRs.
- Generated output follows ordered headings while all facts, examples, paths, and conventions derive from that project or explicit decisions.
- Scenarios cover an existing backend, a UI project, and an empty or undecided project; absent UI/storage does not create empty optional files or invented sections.
- Static navigation walkthroughs start from CLAUDE, follow AGENTS, and reach architecture, a relevant spec, and execution guidance as appropriate. Verify actual destination and section existence.
- Overlapping-domain tasks select all affected specs using discriminating scope, not a generic keyword alone.
- Both references work from an isolated skill installation without sibling packages or paths back into the source repository.
- Synchronization check is read-only, detects either missing or stale reference, and write mode repairs declared targets while preserving unrelated files.
- Missing canonical input fails before any reference target is modified.
- Approval, draft status, legacy preservation, and language rules retain their existing behavior.

## Implementation Boundary

Changes belong only to this skills repository: the standard, new guide, distribution script/tests, four consumer skills and bundled references, applicable scenario documentation, and repository overview. Do not modify the Fingerspot backend. No production implementation is authorized until the user approves this design and its plan.
