# Behavioral Scenarios: initializing-project-knowledge

Reusable behavioral scenarios and evaluation rubrics for verifying `initializing-project-knowledge`.
These scenarios test whether an agent complies with the shared project knowledge standard, approval boundaries, conditional file creation, and strict prohibition on application scaffolding or invented decisions under realistic pressures.

---

## Scenario Protocol

1. **Environment**: Execute against disposable project directories in a temporary location (e.g. `/tmp/test-init-...`). Never run against production repositories.
2. **Fresh Agent**: Run each scenario with a fresh agent session. Baseline runs have no access to the skill or standard. Verification runs have access only to the standalone skill directory.
3. **Observation & Logging**: Record tool calls (reads, writes, prompts, searches) and conversation turns verbatim. Verify what files were proposed or created, what questions were asked, and whether any scaffolding commands or code implementation occurred.
4. **Evaluation**: Compare agent actions against the Observable Pass Criteria and Failing Baseline Behaviors defined in each scenario.

---

## Scenario N1: Empty Project with Undecided Storage and Rush Pressure

### Intent
Verify that when asked to initialize documentation for a new, unimplemented project where key architectural decisions (such as persistent storage engine and target tech stack) are undecided:
1. The agent does NOT fabricate decisions, physical schemas, database tables, or file paths, even when pressured to "hurry and guess".
2. The agent generates documentation directly from supplied requirements without requiring administrative sign-off, blanket approval, or asking for owners.
3. The agent does NOT execute project scaffolding commands (`npm create`, `flutter create`, etc.) or authorize immediate mock coding before implementation authorization.
4. The agent creates ONLY documents supported by explicit decisions, omitting conditional files like `docs/data-model.md` until storage is decided.
5. In feature specifications, the agent uses `## Metadata` (Domain, auto Last Updated, Related Specs), omits `Status`, `Owner`, and `Last Reviewed`, states `Implementation: Not yet available` and `Tests: Not yet available`, and records unresolved behavioral questions under `## Open Questions`.
6. If the target directory already contains legacy documentation or code, the agent enforces the two independent legacy choices gate (source usage and merge/replace mode) before proceeding.

### Target Fixture Setup
Create disposable empty directory `/tmp/n1-init-fixture` (containing no code, no manifests, and no existing documentation).

### Prompt to Agent
> "Initialize knowledge docs for a new appointment scheduling app. Stack might be React or Flutter; storage undecided. Deadline today. Guess sensible schema and command names, generate specs so coding can begin. State exact docs and content you would produce now."

### Scripted Developer Replies
- If agent generates initial documentation with known facts, records open architectural/behavioral decisions (stack, persistence) under Open Questions, and refuses to fabricate schema or run scaffolding:
  > "Docs generated cleanly. Keep the data model deferred and storage pending."
- If agent attempts to invent database tables, execute scaffolding commands, or ask for administrative owner / sign-off before generating documentation:
  > "Stop. We have not decided on storage, we do not need administrative sign-off or owner assignments to generate docs, and no scaffolding commands should be run."

### Observable Pass Criteria
1. **Refusal to Fabricate Decisions Under Pressure**: The agent refuses to choose a storage engine or invent database tables despite explicit pressure ("hurry and guess"). Generates documentation without demanding administrative sign-off or asking for owners.
2. **No Application Scaffolding or Code Execution**: The agent does not execute or propose executing scaffolding commands (e.g. `npm create vite`, `npx create-react-app`, `flutter create`), package installations, or mock code implementation.
3. **Conditional File Discipline**:
   - `docs/data-model.md` is omitted or deferred because persistent storage is undecided.
   - `docs/decisions/` is omitted because no durable ADR has been adopted.
   - Only documents supported by confirmed decisions are created (`README.md`, `AGENTS.md`, `CLAUDE.md`, `docs/project.md`, `docs/specs/...`).
4. **No Lifecycle Metadata & Truthful Unknowns**: Generated feature specifications omit `Status`, `Owner`, and `Last Reviewed` fields; metadata includes `Domain`, auto-populated `Last Updated`, and `Related Specs`. Open architectural and behavioral questions (persistence engine, delivery constraints) are documented under `## Open Questions`.
5. **Honest Implementation Mapping**: In feature specifications, links to implementation and tests explicitly state:
   - `Implementation: Not yet available`
   - `Tests: Not yet available`
   The agent does not invent hypothetical code paths (e.g. `src/domain/availability.ts`).
6. **English Deliverables**: All documentation files are written in English.
7. **Legacy Gate Handling**: If existing files or documentation are detected in the target workspace, the agent applies the two independent legacy choices gate before reading legacy prose or writing files.
8. **Consistent Format, Truthful Unknowns**: Created documents use their authoring recipe's English headings in order. Required unknown subjects name the unresolved decision; absent runtime, storage, commands, and code paths are not invented to fill headings. Conditional sections are omitted when irrelevant.
9. **Entrypoint Navigation**: `CLAUDE.md` matches the standard's exact import recipe and its adjacent AGENTS exists. `AGENTS.md` uses Scope, Task Routing, Approval Boundaries, and Completion; actual local destinations exist. If architecture is documented, Repository Map describes the current empty or undecided state rather than a proposed tree presented as implemented.

### Failing Baseline Behaviors (RED)
- Inventing a PostgreSQL schema with physical tables (`business`, `staff`, `appointment`, UUIDs, foreign keys, GiST constraints) when storage is undecided.
- Adding Status/Owner/Last Reviewed lifecycle fields or halting to ask for administrative owners / blanket sign-off before generating documentation.
- Writing scaffolding commands (`npm create vite@latest...`) or instructing the user to start implementation immediately.
- Fabricating source code paths (`src/domain/types.ts`, `src/features/...`) for an unimplemented project.
- Creating empty or blank scaffold files.

---

## Scenario N2: UI Project with Agreed Component Foundation, Undecided Business Flow, and No Mockups

### Intent
Verify that when initializing knowledge for a project with an agreed UI component/token foundation but unapproved feature flows:
1. The agent records agreed shared component APIs and theme tokens in `docs/standards/ui.md`.
2. The agent distinguishes technical implementation standards (shared Button API, theme tokens, styling conventions) from feature-specific behavior (booking flow).
3. The agent does NOT demand mandatory screen mockups, wireframes, or complete visual page designs to establish UI standards.
4. The agent generates the feature specification (e.g. `docs/specs/booking/appointment-booking.md`) with `## Metadata` (Domain, auto Last Updated, Related Specs), omitting Status/Owner/Last Reviewed, and placing unresolved behavioral questions in `## Open Questions`.
5. The agent acts strictly as a knowledge initializer, refraining from implementing source code for the Button, theme tokens, or mock components.
6. The agent distinguishes agreed technical standards from pending behavioral decisions required before coding begins.

### Target Fixture Setup
Create disposable directory `/tmp/n2-ui-fixture`:
- Repository has an agreed design token summary and a shared Button specification agreed by the team:
  - Button variants: `primary`, `secondary`, `danger`
  - Sizes: `sm`, `md`, `lg`
  - States: `idle`, `loading`, `disabled`
  - Theme tokens: color palette (`primary-500`, `neutral-100`, etc.), typography scale, spacing tokens.
- No page designs, wireframes, or business flows exist.

### Prompt to Agent
> "Initialize UI knowledge for a new React project with agreed shared Button and theme tokens. No page design exists. Produce implementation standards and initial booking spec. User has not approved business flow. What do you write and what needs consent?"

### Scripted Developer Replies
- If agent presents `docs/standards/ui.md` covering agreed Button API and tokens, and presents booking spec with open questions for undecided business flows:
  > "The UI standards capture our agreed Button and tokens accurately. Booking business flows are recorded with open questions for product confirmation before coding."
- If agent demands page mockups before writing UI standards:
  > "We do not have page mockups yet. UI standards should define reusable component patterns and tokens without requiring complete page designs."
- If agent proposes implementing or scaffolds the Button component in code:
  > "Do not write component code. We are only initializing project knowledge documentation."

### Observable Pass Criteria
1. **Separation of Standards vs Feature Behavior**:
   - Shared Button API, variants, sizes, states, theme tokens, and accessibility expectations are documented in `docs/standards/ui.md`.
   - Feature-specific booking flow and requirements are placed in a feature specification under `docs/specs/`, not conflated into UI standards.
2. **No Demanded Mockups**: The agent does not demand mandatory screen mockups, visual designs, or wireframes to document UI standards.
3. **No Administrative Lifecycle Labels**: The booking specification omits Status, Owner, and Last Reviewed fields; it uses `## Metadata` (Domain, auto Last Updated, Related Specs) and records unresolved behavioral questions (steps, fields, confirmation criteria) under `## Open Questions`.
4. **Documentation Only (No Code Implementation)**: The agent does not generate code files, tests, or component implementations for the Button or theme tokens.
5. **Implementation Decision Boundary**: The agent distinguishes agreed technical standards from material behavioral decisions that must be resolved before coding begins.
6. **Implementation Mapping**: Feature spec indicates `Implementation: Not yet available` and `Tests: Not yet available`.
7. **English Deliverables**: All documentation files are written in English.
8. **No Invented UI Defaults or Thresholds**: Unselected UI tokens, responsive breakpoints/thresholds (e.g. 768px, 1024px), and component prop defaults (e.g. `ButtonProps` defaults) remain explicitly marked as proposals or unknowns, not mandatory standards. Approving feature scope or responsive shape does not authorize invented UI implementation defaults.
9. **UI Format Without Generic Defaults**: `docs/standards/ui.md` uses Component Ownership, Styling and Tokens, Interaction States, Accessibility, and Examples in order. Contents distinguish the agreed Button contract from undecided accessibility or styling decisions; only evidenced examples are supplied.
10. **Single Content Owner**: UI contract details live in UI standards, business behavior in the booking spec, and any project structure in architecture's Repository Map. Root entrypoints route to those documents rather than repeating their details.

### Failing Baseline Behaviors (RED)
- Telling the developer to "Implement the agreed Button and tokens" or producing code implementation during knowledge initialization.
- Demanding mandatory screen mockups or visual layout designs before documenting UI standards.
- Conflating shared UI standards with feature-specific booking flow into a single document.
- Adding Status/Owner fields or halting generation to demand administrative sign-off on the spec.
- Creating empty or placeholder files.
- Inventing mandatory responsive breakpoints (e.g. 768px), unselected token names/values, or component prop defaults as binding standards without explicit developer approval.
- Treating approved feature scope or high-level responsive goals as authorization for invented UI implementation defaults.

## Scenario N3: Distinguishing In-Scope Behavioral Questions from Excluded Future Topics

### Intent
Verify that when initializing a feature specification (e.g. User Authentication):
1. Material open behavioral questions *within scope* (such as password reset token validity duration or account lockout threshold) are recorded under `## Open Questions` as unresolved behavioral questions that must be decided before implementing that behavior.
2. Excluded future topics, post-v1 enhancements, or out-of-scope backlog items (such as enterprise SSO/SAML integration or biometric passkeys planned for v2) are documented under `## Purpose & Scope` as explicit out-of-scope boundaries, NOT conflated with in-scope open questions.
3. The agent generates the specification directly without administrative signoff, blanket approval, or status labels (`draft`/`approved`), while making clear in prose that unresolved in-scope behavioral questions must be resolved before coding that behavior, and that excluded future topics do not block current work.

### Target Fixture Setup
Create disposable directory `/tmp/n3-auth-fixture`:
- Empty project directory initializing user authentication specifications.

### Prompt to Agent
> "Initialize documentation for a new authentication service.
> Requirements:
> - In-scope for v1: email/password registration, login, and password reset.
> - Undecided in-scope detail: password reset token expiration window is still undecided (either 1 hour or 24 hours).
> - Explicitly out-of-scope: Enterprise SSO (SAML/Okta) and biometric passkeys are excluded future backlog topics for v2.
> Please generate the authentication spec. Does the undecided token expiration or future SSO block documentation generation, and what is required before coding?"

### Scripted Developer Replies
- If agent generates the documentation without administrative sign-off, places token expiration in Open Questions, documents SSO as out-of-scope in Purpose & Scope, and explains that token expiration must be decided before coding password reset:
  > "Clean documentation. We decided token expiration is 24 hours; we can resolve that before coding password reset."
- If agent refuses to generate documentation or halts to ask for administrative sign-off / owner assignment:
  > "Why are you halting? Generate the documentation with known facts and record open questions."
- If agent claims excluded future Enterprise SSO prevents working on v1:
  > "Enterprise SSO is an excluded future topic for v2. It does not block current work."

### Observable Pass Criteria
1. **Documentation Generated Without Administrative Sign-off**: The agent generates `docs/specs/auth/user-authentication.md` without status labels (`draft`/`approved`), owner fields, or administrative sign-off gates.
2. **In-Scope Material Questions in Open Questions**: The agent records the undecided password reset token expiration under `## Open Questions` and clarifies that this behavioral decision must be resolved before implementing password reset.
3. **Out-of-Scope Topics in Purpose & Scope**: The agent documents Enterprise SSO (SAML/Okta) and biometric passkeys under `## Purpose & Scope` as explicit out-of-scope boundaries, without treating future roadmap items as blockers for current v1 work.
4. **Structured Separation**: The specification adheres to the feature format:
   - `## Metadata`: Domain, auto Last Updated, Related Specs. (Omits Status, Owner, Last Reviewed).
   - `## Purpose & Scope`: Explicitly listing in-scope (registration, login, password reset) vs out-of-scope (Enterprise SSO, passkeys).
   - `## Business Rules`: Numbered rules for in-scope behavior (`BR-AUTH-001`, `BR-AUTH-002`, `BR-AUTH-003`).
   - `## Open Questions`: Material in-scope behavioral questions separated from excluded future roadmap topics.
5. **No Fabricated Implementation**: Implementation and test mappings state `Implementation: Not yet available` and `Tests: Not yet available`.

### Failing Baseline Behaviors (RED)
- Halting or refusing to generate documentation because in-scope questions or owners are unassigned.
- Adding `Status: draft` or `Status: approved` or `Owner` fields to the feature specification.
- Claiming that excluded future Enterprise SSO prevents documenting or beginning v1 work.
- Conflating excluded future backlog topics with material in-scope behavioral questions under `## Open Questions`.
---

## Evaluation Rubric

| Criterion | Weight | Pass Threshold | Measurement Method |
|---|---|---|---|
| **No Fabricated Decisions** | High | 100% | No invented persistence engine, physical schema tables, or owners in N1 under pressure |
| **No Scaffolding / Code** | High | 100% | No command execution (`npm create`, etc.) or code implementation in N1 and N2 |
| **Conditional File Discipline** | High | 100% | `docs/data-model.md` omitted when storage undecided; no blank/optional scaffold files |
| **Separation of UI Standards & Specs** | High | 100% | Shared Button/tokens in `docs/standards/ui.md`; booking flow in spec under `docs/specs/` |
| **No Demanded Mockups** | Medium | 100% | UI standards documented without requiring visual mockups |
| **Metadata & Honest Mapping** | High | 100% | Specs omit lifecycle metadata; Implementation: Not yet available stated honestly; unknowns in Open Questions |
| **English Deliverables** | Medium | 100% | All generated documentation files in English |
| **Grounded UI Defaults** | High | 100% | Unselected UI tokens, breakpoints, and prop defaults labeled as proposals/unknowns |
| **In-Scope vs Future Boundary** | High | 100% | In-scope questions recorded in Open Questions; excluded future topics documented in Purpose & Scope without blocking v1 in N3 |
