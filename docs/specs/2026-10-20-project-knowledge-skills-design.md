# Project Knowledge Skills Design

## Status and intent

Proposed design for joint approval with its implementation plan. The file layout and behavioral requirements below reflect the conversation; concrete packaging and validation choices explicitly marked **Design call** are recommendations, not prior user decisions.

Build four reusable, English-language skills for general coding agents. They establish repository knowledge from existing or new projects, guide subsequent changes, and audit alignment. The primary objective is preventing silent divergence from approved business behavior and coding standards. Onboarding and navigation support that objective.

The workspace currently contains no existing project files and is not a Git repository. Writing this design does not authorize initializing Git, installing skills, generating target-project documentation, or changing application code. Design/plan commits require Git initialization approval; do not initialize merely to satisfy a workflow convention.

## Agreed requirements

- Deliver `documenting-existing-projects`, `initializing-project-knowledge`, `working-with-project-specs`, and `auditing-project-knowledge`, beginning implementation with the existing-project generator.
- All skill content and generated documentation are English. Conversation follows the user's language. Preserve code identifiers, product names, and meaningful domain terminology; confirm uncertain translations.
- Use `AGENTS.md` as the shared instruction entrypoint. Always generate `CLAUDE.md` solely as an entrypoint directing Claude to read `AGENTS.md`; do not duplicate rules.
- Support general coding agents without requiring Claude-specific hooks, slash commands, imports, MCP, or automatic skill discovery. Document that actual loading depends on the host runtime.
- Existing-project generation asks two independent questions before reading legacy documentation for meaning or modifying it: whether legacy documentation may be used as a source, and whether existing documents should be merged or replaced. Explicit answers already given for the current run need not be asked again.
- Every discrepancy between approved specs, observed code behavior, and requested behavior is brought to the developer. No automatic choice of authority, even when code looks newer or the request sounds explicit.
- An implementation request is not approval to change a conflicting spec. Obtain explicit approval for the identified spec change first, update the spec, then implement the approved behavior.
- A feature with no spec requires a new draft spec and developer approval before implementation.
- Investigation may continue to establish evidence and impact. Mutations implementing the unresolved behavior or updating the approved spec wait for developer decisions. Unrelated work must not conceal unresolved conflicts.
- Do not generate a `changes/` directory, proposal archive, approval log, or per-change document. Confirmation happens in conversation; ordinary Git history records document changes when Git exists.
- UI standards live at `docs/standards/ui.md`, not a separate `DESIGN.md`. They govern components, layouts, themes, interaction patterns, UI states, accessibility, and code examples—not mandatory screen mockups.
- Feature specs include relevant ERDs, table roles, relevant columns/constraints, and the data read or changed at each flow step. A shared application model supplies cross-feature context. Do not force data diagrams onto features without persistence.

## Goals and non-goals

Goals: shared document responsibilities; evidence-based discovery; explicit decisions at behavioral boundaries; minimal generated documentation; predictable English output; portable, testable skills.

Non-goals: implementing application features as part of generation; changing stack or architecture; designing a developer portal; installing a documentation framework; enforcing semantic correctness solely through Markdown; adopting every tool used by large companies; replacing existing coding/review workflows wholesale.

Anti-goals: blessing observed bugs as approved rules; silently overwriting legacy material; generating empty documentation trees; maintaining separate Claude rules; approving unresolved behavior through an automated audit; inventing owners, schema details, paths, verification results, or developer consent.

## Target repository documentation contract

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
    ui.md                       # when UI exists
  workflows/
    spec-changes.md
  specs/
    README.md
    <domain>/
      <feature>.md
```

Optional `docs/decisions/` is introduced only when a durable technical decision warrants a separate record. Initially put concise architectural rationale in `architecture.md`. Never generate optional files as empty scaffolds.

Document responsibilities:

- Root README: concise introduction and route to setup/documentation. `docs/README.md`: task-oriented navigation, not another project description.
- AGENTS: concise mandatory agent instructions, contextual reading routes, stop/confirmation rules, links to standards and the workflow. It is a map, not the full manual.
- CLAUDE: plain English instruction and relative link to AGENTS. **Design call:** use ordinary Markdown rather than tool-specific import syntax; verify that an agent actually follows it instead of claiming host-independent automatic loading.
- Project: purpose, users, domain glossary, stack overview with links to authoritative manifests. Do not manually duplicate dependency versions from lockfiles.
- Architecture: module responsibilities, boundaries, dependencies, and key rationale. Data model: application-wide entity/relationship map, definitions, and links to physical schema. Break large diagrams by domain rather than making one unreadable diagram.
- Development: prerequisites, setup, local execution, configuration names without secret values, verification commands, troubleshooting. Other documents link rather than duplicating command inventories.
- Coding/testing/UI standards: distinct implementation rules with representative real examples and links to enforcing tools. Observed conventions must be distinguished from developer-approved policy during initial discovery.
- Spec workflow: conflict presentation, new-spec drafting, approval, update-before-implementation, and post-change verification/documentation updates. No separate proposal artifact.
- Specs index: feature navigation plus the shared format. Do not emit a separate template file into every target repository.

Feature specs use consistent headings: identity/status; purpose/scope/terms; business rules with stable IDs; relevant model/ERD; flows with data access; failure and consistency behavior; observable acceptance criteria; contracts/dependencies; implementation/test links; material open questions. Status `draft` or `approved` describes specification approval only, not implementation completion. Open behavioral questions prevent approval. Sections may state briefly that they do not apply; do not invent diagrams, API contracts, or physical paths to fill a template. Before code exists, implementation mapping explicitly says it is not yet available rather than fabricating links.

A feature ERD is a view of the shared model, not an independent schema. Relationships do not imply business policies: a User–Subscription relation alone does not prove that addon purchase requires an active subscription. Physical schema disagreements are developer questions. Critical behavior must remain explicit in prose and acceptance criteria.

## Common approval and evidence contract

Present each material conflict with: approved rule/source; observed or requested difference and evidence location; known impact; unresolved questions; the specific decision required. Do not ask the developer for facts reachable through permitted tools. Never infer that approving one change approves related pricing, entitlement, data, or UI behavior.

Approval is explicit, contextual developer consent to a concrete draft or identified change. Scope-changing edits after approval require renewed consent. Do not fabricate an approval identity or timestamp. Do not persist conversation transcripts or approval records as new project artifacts. A spec may be marked approved only after genuine consent; its normal content and Git history suffice.

Separate static observations from exercised behavior and hypotheses. Existing tests are evidence of expectations, not automatic proof of business intent. Commands may be published only if grounded in actual scripts/configuration or verified help; claim execution only when exercised. Do not run installations, migrations, production operations, or target applications merely to infer a policy.

## Skill responsibilities

### documenting-existing-projects

Inputs: target path, legacy-source choice, merge/replace choice, and developer decisions.

1. Inspect filenames and detect documentation presence without consuming legacy prose as authority. Batch the two choices if missing.
2. Discover code, manifests, schemas/migrations, test behavior and component/theme implementations as relevant. **Design call:** known legacy docs may be read after a no-source choice only for a clearly explained preservation operation under merge, not to infer policy. Ask permission before content reads that could otherwise violate the choice. If content reading is disallowed entirely, preserve those files untouched and propose additive edits elsewhere; confirm any collisions.
3. Use scoped scouts when the runtime supports them; otherwise perform the same exploration inline. For the future `tnc-backend` use case, the user specifically requests scouts and excludes Markdown/legacy documentation as sources. Do not start that exploration during this design stage.
4. Present feature coverage, evidence, uncertainties, target-file mapping and impacted existing content. Code-derived business rules remain draft until confirmed. Missing business intent is not filled with generic best practices.
5. Merge preserves relevant content, resolves duplicates deliberately and confirms semantic conflicts. Replace covers only disclosed files; obtain specific confirmation before removing, relocating or overwriting unrelated or unique material. Do not delete all docs by default.
6. After required approvals, write grounded documentation and verify links, applicable structure, consistent ERDs and the actual agent reading route. A requested preservation area is not silently translated or rewritten outside scope.

Outputs: documentation and a concise in-conversation verification/remaining-decision report, not additional discovery artifacts in the target repo. Actual approvals may cover a coherent batch of clearly described specs; do not require one ritual per sentence.

### initializing-project-knowledge

Reuse the same contract for an unimplemented project. Gather purpose, scope, intended stack, architecture, conventions and initial features; create only grounded documents. Clearly label proposed decisions. New specs are drafts until approved. No dependency installation, application scaffolding, or invented physical schema is part of this skill. Architecture/data choices become concrete only as decided; update mappings after implementation through the working skill.

### working-with-project-specs

Locate affected specs and standards before changes. Treat missing, ambiguous, mutually conflicting, or code-divergent behavior as a confirmation boundary. Show conflicts in conversation; use a new draft in the final feature-spec location when needed, not a proposals folder. Following approval, update the spec before implementation, then update other affected docs and actual implementation/test links. For behavior-preserving changes, do not edit spec semantics or refresh dates without a real review. Reuse the host's implementation, testing and review practices; do not write a second general coding lifecycle.

### auditing-project-knowledge

Read-only by default. Evaluate structural coverage, broken references, stale implementation maps, spec/code/schema divergence, standards conflicts, and instruction routing. Report severity, evidence, affected document/rule, and the developer decision or correction needed. Separate automatic structural findings from uncertain semantic judgments. An audit neither grants spec approval nor automatically rewrites code/docs. Fixing findings requires an authorized generation or working workflow.

## Packaging — design calls

Use four self-contained skill directories at the repository root, each containing `SKILL.md` and `references/project-knowledge-standard.md`. Maintain one authoritative source at `shared/project-knowledge-standard.md` in the authoring repository. A small Python-standard-library script `scripts/sync-references.py` synchronizes the four packaged copies and supports `--check` without mutation. Copies are distribution outputs, not independently maintained policies.

This avoids mandatory sibling-directory links that break when a user installs one skill. Each skill reads its own bundled standard on demand. Use relative supporting-file links; do not require runtime-specific tools. No external package dependencies, custom host configuration, automatic global installation or new target-project config formats.

User-facing repository README documents installation as directory copying according to each runtime, entrypoint-loading limitations, invocation examples and the shared-standard maintenance command. Do not claim installation was performed.

## Verification and acceptance

Skill verification uses fresh-agent scenarios with a no-skill baseline before authoring the corresponding skill, followed by the same scenarios with the skill. Record actual outcomes; baseline compliance is not a failing test. Use targeted scenario variants to expose real missing guidance, not arbitrary failure claims. No product skill is written before its baseline behavior is observed.

Essential scenarios: two independent legacy choices; no-source plus merge; conflicting code/spec/request; missing spec; scope-expanding consent; non-English legacy content; backend with no UI; UI with reusable components; incomplete future schema; read-only audit; single-directory installation; thin CLAUDE entrypoint.

Mechanical checks verify packaged-reference parity, local Markdown links and entrypoints on throwaway examples; behavior is tested through agent actions, not source-text assertions. Smoke validation includes a generated backend and UI knowledge base, loading CLAUDE then following AGENTS, a stopped conflicting request, an explicitly approved update, and a read-only audit with known findings. Generated fixtures and run transcripts are verification material, not additional files generated into user projects.

**Design call:** keep reusable behavioral scenario prompts and a human-readable rubric under `tests/scenarios/`; run-specific observations go to a temporary/local artifact unless the repository later has an established evidence convention. Do not add an LLM SDK dependency or pretend subjective semantic review is a deterministic unit test.

Completion means four usable, independently packaged skills, one synchronized standard, demonstrated approval boundaries, documented verification outcomes and no modifications to the application use case. `tnc-backend` exploration and documentation generation are a subsequent invocation requiring the developer's source and write-mode decisions.

## Research basis and limits

- Google documents team-approved design templates, ownership, review and freshness: https://abseil.io/resources/swe-book/html/ch10.html
- One OpenAI team describes a short AGENTS map and structured repository knowledge: https://openai.com/index/harness-engineering/
- Anthropic recommends concise shared instructions and context loaded when relevant: https://code.claude.com/docs/en/best-practices
- Spotify describes shared catalog context for humans and agents: https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint

These support the principles, not the exact filenames, four-skill decomposition, per-feature ERD requirement or packaging design. Those are adaptations to this user's requirements.
