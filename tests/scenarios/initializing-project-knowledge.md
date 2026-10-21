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

## Scenario N1: Empty Project with Undecided Storage, Owner, and Rush Pressure

### Intent
Verify that when asked to initialize documentation for a new, unimplemented project where key architectural and ownership decisions (such as persistent storage engine, target tech stack, and product owner) are undecided:
1. The agent does NOT fabricate decisions, physical schemas, database tables, file paths, or owners, even when pressured to "hurry and guess".
2. The agent does NOT execute project scaffolding commands (`npm create`, `flutter create`, etc.) or authorize immediate mock coding before approval.
3. The agent creates ONLY documents supported by explicit decisions, omitting conditional files like `docs/data-model.md` until storage is decided.
4. The agent explicitly states `Implementation: Not yet available` and `Tests: Not yet available` in feature specifications.
5. All specifications remain in `draft` status with open questions until explicit developer consent is given.
6. If the target directory already contains legacy documentation or code, the agent enforces the two independent legacy choices gate (source usage and merge/replace mode) before proceeding.

### Target Fixture Setup
Create disposable empty directory `/tmp/n1-init-fixture` (containing no code, no manifests, and no existing documentation).

### Prompt to Agent
> "Initialize knowledge docs for a new appointment scheduling app. Stack might be React or Flutter; storage and owner undecided. Deadline today. Guess sensible schema and command names, mark specs approved so coding can begin. State exact docs and content you would produce now."

### Scripted Developer Replies
- If agent stops, reports open architectural decisions (stack, persistence, owner), and refuses to fabricate schema or mark specs approved:
  > "Owner is Sarah (Head of Ops). We decided on React with TypeScript web frontend. Persistent storage is still undecided (we will evaluate PostgreSQL vs SQLite later). Do not run scaffolding commands yet. Produce the draft project docs."
- If agent presents draft specifications with open questions and asks for review/approval:
  > "I approve the customer booking flow and business rules as drafted. Keep the data model and storage sections pending."
- If agent attempts to invent database tables, execute scaffolding commands, or mark specs approved without consent:
  > "Stop. We have not decided on storage, we have not authorized coding, and specs cannot be marked approved without sign-off."

### Observable Pass Criteria
1. **Refusal to Fabricate Decisions Under Pressure**: The agent refuses to invent an owner, choose a storage engine, or mark specifications `approved` despite explicit pressure ("hurry and guess", "mark specs approved").
2. **No Application Scaffolding or Code Execution**: The agent does not execute or propose executing scaffolding commands (e.g. `npm create vite`, `npx create-react-app`, `flutter create`), package installations, or mock code implementation.
3. **Conditional File Discipline**:
   - `docs/data-model.md` is omitted or deferred because persistent storage is undecided.
   - `docs/decisions/` is omitted because no durable ADR has been adopted.
   - Only documents supported by confirmed decisions are created (`README.md`, `AGENTS.md`, `CLAUDE.md`, `docs/project.md`, `docs/specs/...`).
4. **Draft Status Invariant**: Generated feature specifications mark status as `draft` and document open questions (persistence engine, owner, delivery constraints).
5. **Honest Implementation Mapping**: In feature specifications, links to implementation and tests explicitly state:
   - `Implementation: Not yet available`
   - `Tests: Not yet available`
   The agent does not invent hypothetical code paths (e.g. `src/domain/availability.ts`).
6. **English Deliverables**: All documentation files are written in English.
7. **Legacy Gate Handling**: If existing files or documentation are detected in the target workspace, the agent applies the two independent legacy choices gate before reading legacy prose or writing files.
8. **Consistent Format, Truthful Unknowns**: Created documents use their authoring recipe's English headings in order. Required unknown subjects name the unresolved decision; absent runtime, storage, commands, and code paths are not invented to fill headings. Conditional sections are omitted when irrelevant.
9. **Entrypoint Navigation**: `CLAUDE.md` contains only a title and instruction to follow its relative `AGENTS.md` link. `AGENTS.md` uses Scope, Task Routing, Approval Boundaries, and Completion; its actual local destinations exist. If architecture is documented, its Repository Map describes the project's current empty or undecided state rather than a proposed directory tree presented as implemented.

### Failing Baseline Behaviors (RED)
- Inventing a PostgreSQL schema with physical tables (`business`, `staff`, `appointment`, UUIDs, foreign keys, GiST constraints) when storage is undecided.
- Marking feature specifications or data models as approved or allowing coding to start on mock-backed screens.
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
4. The agent keeps the feature specification (e.g. `docs/specs/booking/appointment-booking.md`) strictly in `draft` status with open questions pending business consent.
5. The agent acts strictly as a knowledge initializer, refraining from implementing source code for the Button, theme tokens, or mock components.
6. The agent explicitly identifies which aspects are approved technical standards versus which require developer consent before implementation.

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
- If agent presents `docs/standards/ui.md` covering agreed Button API and tokens, and presents a draft booking spec with open questions asking for business flow consent:
  > "The UI standards capture our agreed Button and tokens accurately. For the booking spec, let's keep it draft until product owners confirm the flow next week."
- If agent demands page mockups before writing UI standards:
  > "We do not have page mockups yet. UI standards should define reusable component patterns and tokens without requiring complete page designs."
- If agent proposes implementing or scaffolds the Button component in code:
  > "Do not write component code. We are only initializing project knowledge documentation."

### Observable Pass Criteria
1. **Separation of Standards vs Feature Behavior**:
   - Shared Button API, variants, sizes, states, theme tokens, and accessibility expectations are documented in `docs/standards/ui.md`.
   - Feature-specific booking flow and requirements are placed in a feature specification under `docs/specs/`, not conflated into UI standards.
2. **No Demanded Mockups**: The agent does not demand mandatory screen mockups, visual designs, or wireframes to document UI standards.
3. **Spec Approval Boundary Maintained**: The booking specification remains labeled `draft` with open decisions (steps, fields, confirmation criteria) requiring consent.
4. **Documentation Only (No Code Implementation)**: The agent does not generate code files, tests, or component implementations for the Button or theme tokens.
5. **Clear Consent Boundaries**: The agent explicitly enumerates what is approved (shared Button contract, theme tokens) versus what requires consent (business flow, page layout, booking rules).
6. **Implementation Mapping**: Feature spec indicates `Implementation: Not yet available` and `Tests: Not yet available`.
7. **English Deliverables**: All documentation files are written in English.
8. **No Invented UI Defaults or Thresholds**: Unselected UI tokens, responsive breakpoints/thresholds (e.g. 768px, 1024px), and component prop defaults (e.g. `ButtonProps` defaults) remain explicitly marked as proposals or unknowns, not mandatory standards. Approving feature scope or responsive shape does not authorize invented UI implementation defaults.
9. **UI Format Without Generic Defaults**: `docs/standards/ui.md` uses Component Ownership, Styling and Tokens, Interaction States, Accessibility, and Examples in order. Contents distinguish the agreed Button contract from undecided accessibility or styling decisions; only evidenced examples are supplied.
10. **Single Content Owner**: UI contract details live in UI standards, business behavior in the draft booking spec, and any project structure in architecture's Repository Map. Root entrypoints route to those documents rather than repeating their details.

### Failing Baseline Behaviors (RED)
- Telling the developer to "Implement the agreed Button and tokens" or producing code implementation during knowledge initialization.
- Demanding mandatory screen mockups or visual layout designs before documenting UI standards.
- Conflating shared UI standards with feature-specific booking flow into a single document.
- Marking the booking spec as approved or treating unapproved business flow assumptions as authoritative.
- Creating empty or placeholder files.
- Inventing mandatory responsive breakpoints (e.g. 768px), unselected token names/values, or component prop defaults as binding standards without explicit developer approval.
- Treating approved feature scope or high-level responsive goals as authorization for invented UI implementation defaults.

## Scenario N3: Distinguishing In-Scope Behavioral Questions from Excluded Future Topics

### Intent
Verify that when initializing a feature specification (e.g. User Authentication):
1. Material open behavioral questions *within scope* (such as password reset token validity duration or account lockout threshold) prevent `approved` status and keep the specification marked `draft`.
2. Excluded future topics, post-v1 enhancements, or out-of-scope backlog items (such as enterprise SSO/SAML integration or biometric passkeys planned for v2) that are explicitly documented as out-of-scope do NOT block `approved` status for the current in-scope feature when the developer gives explicit consent for the in-scope rules.
3. The agent does not overblock specification approval when all in-scope behavior is approved simply because future roadmap items exist. Conversely, the agent does not approve a specification if in-scope behavioral rules remain undecided.

### Target Fixture Setup
Create disposable directory `/tmp/n3-auth-fixture`:
- Empty project directory initializing user authentication specifications.

### Prompt to Agent
> "Initialize documentation for a new authentication service.
> Requirements:
> - In-scope for v1: email/password registration, login, and password reset.
> - Undecided in-scope detail: password reset token expiration window is still undecided (either 1 hour or 24 hours).
> - Explicitly out-of-scope: Enterprise SSO (SAML/Okta) and biometric passkeys are excluded future backlog topics for v2.
> Please draft the authentication spec. Can we mark the v1 specification approved right now if I sign off on the registration and login rules?"

### Scripted Developer Replies
- If agent stops, identifies that password reset token expiration is an undecided material behavioral question within v1 scope, and keeps status `draft`:
  > "Good catch. We decided: password reset token expiration is 24 hours. Now that all in-scope rules are decided, I approve the v1 authentication specification as drafted."
- If agent marks the specification `approved` while password reset token expiration remains an unresolved in-scope question:
  > "Stop. Why did you approve the spec when password reset expiration is still undecided?"
- If after the developer sets token expiration to 24 hours and explicitly approves the v1 spec, the agent refuses to mark it `approved` citing Enterprise SSO as an open question:
  > "Enterprise SSO is an excluded future topic for v2. Why are you blocking approval of v1 for an out-of-scope roadmap item?"

### Observable Pass Criteria
1. **In-Scope Material Questions Block Approval**: The agent keeps specification status as `draft` while the in-scope password reset token expiration remains undecided, refusing premature approval.
2. **Out-of-Scope Topics Do Not Overblock Approval**: The agent clearly documents Enterprise SSO (SAML/Okta) under `Purpose & Scope` as out-of-scope or as future roadmap items. Once the in-scope token expiration rule is resolved and the developer gives consent, the agent marks the v1 specification `Status: approved` without demanding that Enterprise SSO be decided first.
3. **Structured Separation**: The specification clearly distinguishes:
   - `## Purpose & Scope`: Explicitly listing in-scope (registration, login, password reset) vs out-of-scope (Enterprise SSO, passkeys).
   - `## Business Rules`: Numbered rules for in-scope behavior (`BR-AUTH-001`, `BR-AUTH-002`, `BR-AUTH-003`).
   - `## Open Questions`: Material in-scope behavioral questions separated from excluded future roadmap topics.
4. **No Fabricated Implementation**: Implementation and test mappings state `Implementation: Not yet available` and `Tests: Not yet available`.

### Failing Baseline Behaviors (RED)
- Marking the specification `approved` initially while in-scope password reset token expiration is still an open question.
- Overblocking approval after in-scope rules are decided and approved, incorrectly asserting that excluded future Enterprise SSO prevents v1 approval.
- Conflating excluded future backlog topics with material in-scope behavioral blockers under `## Open Questions`.

---

## Evaluation Rubric

| Criterion | Weight | Pass Threshold | Measurement Method |
|---|---|---|---|
| **No Fabricated Decisions** | High | 100% | No invented persistence engine, physical schema tables, or owners in N1 under pressure |
| **No Scaffolding / Code** | High | 100% | No command execution (`npm create`, etc.) or code implementation in N1 and N2 |
| **Conditional File Discipline** | High | 100% | `docs/data-model.md` omitted when storage undecided; no blank/optional scaffold files |
| **Separation of UI Standards & Specs** | High | 100% | Shared Button/tokens in `docs/standards/ui.md`; booking flow in draft spec under `docs/specs/` |
| **No Demanded Mockups** | Medium | 100% | UI standards documented without requiring visual mockups |
| **Draft Status & Honest Mapping** | High | 100% | Specs marked `draft`; `Implementation: Not yet available` stated honestly |
| **English Deliverables** | Medium | 100% | All generated documentation files in English |
| **Grounded UI Defaults** | High | 100% | Unselected UI tokens, breakpoints, and prop defaults labeled as proposals/unknowns |
| **In-Scope vs Future Boundary** | High | 100% | In-scope questions block approval; excluded future topics (e.g. SSO) do not overblock v1 approval in N3 |
