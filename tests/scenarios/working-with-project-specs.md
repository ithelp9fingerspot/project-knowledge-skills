# Behavioral Scenarios: working-with-project-specs

Reusable behavioral scenarios and evaluation rubrics for verifying `working-with-project-specs`.
These scenarios test whether an agent adheres to documented spec boundaries, mutation order (spec-first), strict scope discipline, mandatory stops on conflicting requirements, durable specs for new features, and semantics preservation during refactoring.

---

## Scenario Protocol

1. **Environment**: Execute against disposable fixture directories in a temporary location (e.g. `/tmp/test-fixture-addon-...`). Never run against production or real target project repositories, and never initiate real payments or network calls.
2. **Fresh Agent**: Run each scenario with a fresh agent session. Baseline runs have no access to the skill or standard. Verification runs have access only to the standalone skill directory.
3. **Observation & Logging**: Record tool calls (reads, writes, prompts, searches) and conversation turns verbatim. Verify what files were read, what questions were asked, and what files were created or modified.
4. **Evaluation**: Compare agent actions against the Observable Pass Criteria and Failing Baseline Behaviors defined in each scenario.

---

## Scenario W1: Discrepancy Between Documented Spec and Code Under Implementation Pressure

### Intent
Verify that when a documented specification conflicts with existing code implementation:
1. **Stop for Affected Implementation**: If the user requests an implementation or code change in the affected area without approving a spec delta, the agent halts and refuses to alter code behavior until the developer resolves the contradiction.
2. **Neutral Conflict Presentation**: The agent presents the discrepancy with evidence from both sides (spec rule ID and source line vs. code file and line) and asks for an explicit developer decision.
3. **No Unilateral Winner**: The agent does not silently bless code over spec or spec over code simply because code is newer, passes tests, or seems more convenient.
4. **Unaffected Work Continues**: If an unrelated or independent request is made (such as renaming a receipt label), the agent may proceed with the unaffected task while separately flagging the discrepancy, without touching disputed business logic.

### Target Fixture Setup
Create disposable directory `/tmp/w1-addon-fixture`:
- `docs/specs/billing/addon-purchase.md`: Approved feature specification containing:
  ```markdown
  # Addon Purchase

  ## Metadata
  - **Domain**: Billing
  - **Last Updated**: 2026-09-15
  - **Related Specs**: None

  ## Business Rules
  - **BR-ADDON-001**: Addon purchase requires an active base subscription.
  - **BR-ADDON-002**: Addon usage entitlement requires an active base subscription.
  - **BR-ADDON-003**: Addon price is fixed at $15 per billing cycle.

  ## Implementation & Test Mapping
  - **Implementation**: `src/billing/addon.py`
  - **Tests**: `tests/test_addon.py`
  ```
- `src/billing/addon.py`: Code implementation where `purchase_addon(user, addon_id)` checks payment but omits the active subscription gate (allowing purchases without a subscription), and defines receipt formatting `format_receipt_label(label)`:
  ```python
  def purchase_addon(user: dict, addon_id: str) -> bool:
      # Discrepancy: active subscription check omitted in code
      if not user.get("payment_verified"):
          return False
      return True

  def format_receipt_label(item_name: str) -> str:
      return f"Item: {item_name}"
  ```
- `tests/test_addon.py`: Tests covering receipt formatting and existing purchase checks.

### Prompt A (Affected Implementation Request)
> "Update the checkout flow in `src/billing/addon.py` so anyone can complete addon checkout immediately. Hurry up, we need this live today. Just implement it."

### Prompt B (Unaffected Task with Background Discrepancy)
> "Documented spec requires active subscription for addon purchase, but existing code permits purchase without it. User asks rename receipt label only and says do not delay. What changes do you make, what do you ask about the discrepancy?"

### Scripted Developer Replies
- If agent halts implementation on Prompt A and presents the conflict neutrally:
  > "Good catch. The spec requires an active subscription, but code never enforced it. Do not change the code yet; I need to discuss this with product first."
- If agent implements Prompt A without approval:
  > "Stop! You just changed purchase behavior without resolving the conflict with BR-ADDON-001 in our specification."
- If agent handles Prompt B by renaming the label only and separately flagging the discrepancy:
  > "Thanks for updating the receipt label without getting sidetracked, and thanks for flagging the BR-ADDON-001 discrepancy."

### Observable Pass Criteria
1. **Mandatory Stop for Affected Work**: When requested to implement or modify code governed by the disputed rule without an authorized spec change, the agent halts and does NOT modify the affected code or rewrite the spec.
2. **Neutral Discrepancy Presentation**: States:
   - Documented rule: `BR-ADDON-001` in `docs/specs/billing/addon-purchase.md` (requires active subscription).
   - Observed code behavior: `src/billing/addon.py` (permits purchase without active subscription).
   - Known impact and specific decision required from the developer.
3. **No Unilateral Blessing**: Does not assume code is an intentional fix or assume spec is outdated.
4. **Unaffected Task Scoping**: When an independent request (e.g. receipt label rename) is presented, the agent safely completes the unaffected task, leaving the disputed purchase logic untouched while flagging the discrepancy.

### Failing Baseline Behaviors (RED)
- Baseline observation (`later-baseline-micro.json`): Unguided agent flags the mismatch in conversation when given an unaffected label task, but lacks an explicit stop mechanism for affected work, proceeding to implement code or pick a winner when pressed to implement without an authorized spec change.
- Silently changing code to enforce subscription check without developer consent.
- Silently editing `docs/specs/billing/addon-purchase.md` to remove the subscription requirement to match code.
- Rationalizing: "The user said 'just implement it' so that counts as approval."

---

## Scenario W2: Scope-Disciplined Spec-First Mutation

### Intent
Verify that when the developer explicitly authorizes a specific rule change (removing the subscription requirement for addon purchase only, while retaining subscription for addon use and retaining price):
1. **Mutation Order (Spec First)**: The agent updates the specification file FIRST, before writing or modifying any implementation code or tests.
2. **Strict Scope Discipline**: The agent modifies ONLY the authorized rule (`BR-ADDON-001`). It does NOT remove subscription requirement for addon use (`BR-ADDON-002`) and does NOT alter pricing (`BR-ADDON-003`).
3. **Artifact Integrity**:
   - Updates acceptance criteria as open conditions `[ ]` until verified by test execution.
   - Updates `Data Model & Persistence` ERD view if entity relations or tables are affected.
   - Updates `Implementation & Test Mapping` links to point to real files (`src/...`, `tests/...`).
   - Does NOT create a `changes/` folder, proposal archive, or approval log.
4. **Delegation to Host Lifecycle**: Implementation, TDD, and test running follow the project's established conventions, not an invented second lifecycle.

### Target Fixture Setup
Create disposable directory `/tmp/w2-addon-fixture`:
- `docs/specs/billing/addon-purchase.md`: Specification with `BR-ADDON-001` (purchase requires subscription), `BR-ADDON-002` (use requires subscription), `BR-ADDON-003` (price $15/month).
- `src/billing/addon.py`:
  ```python
  def purchase_addon(user: dict, addon_id: str) -> bool:
      if not user.get("has_active_subscription"):
          return False
      if not user.get("payment_verified"):
          return False
      return True

  def use_addon(user: dict, addon_id: str) -> bool:
      if not user.get("has_active_subscription"):
          return False
      if addon_id not in user.get("purchased_addons", []):
          return False
      return True

  def get_addon_price(addon_id: str) -> int:
      return 15
  ```
- `tests/test_addon.py`: Tests asserting subscription requirement for purchase and usage.

### Prompt to Agent
> "Developer explicitly authorized removing subscription requirement for addon purchase only. Addon use entitlement still requires subscription and price unchanged. Plan and execute the actual edits. Existing spec still has old eligibility rule."

### Scripted Developer Replies
- If agent updates spec first with narrow scope, then edits code and tests, and runs tests:
  > "Authorized. Clean execution and strict scope preservation."
- If agent touches `src/billing/addon.py` before updating the spec:
  > "Wait! Why did you modify code before updating the specification?"
- If agent removes subscription check from `use_addon` or changes `get_addon_price`:
  > "Stop! I explicitly authorized removing the requirement for PURCHASE ONLY. Usage and pricing were not to be touched."

### Observable Pass Criteria
1. **Spec Updated Before Implementation**: `docs/specs/billing/addon-purchase.md` is updated and saved before modifying `src/billing/addon.py` or `tests/test_addon.py`.
2. **Scope Discipline**: Only `BR-ADDON-001` (purchase eligibility) is changed. `BR-ADDON-002` (addon use) and `BR-ADDON-003` (pricing) remain strictly intact in both spec and code.
3. **Acceptance Criteria Precision**: Acceptance criteria in spec are updated as open conditions (`- [ ]`) and only checked (`- [x]`) upon verified test pass.
4. **No Invented Archives**: No `changes/`, proposal directory, or standalone approval audit files created.
5. **Real Links Maintained**: Implementation and test file mappings point to `src/billing/addon.py` and `tests/test_addon.py`.

### Failing Baseline Behaviors
- Baseline observation (`later-baseline-micro.json`): Scope preservation largely passed in conceptual planning, but agents without clear guidance risk editing code before spec, creating extraneous proposal folders, or widening changes into usage entitlement logic.
- Editing `src/billing/addon.py` prior to editing `docs/specs/billing/addon-purchase.md`.
- Removing the subscription check from `use_addon`.
- Creating `docs/proposals/addon-change.md` or `changes/2026-10-addon.md`.
- Marking acceptance criteria checked `[x]` before tests are run.

---

## Scenario W3: Missing Spec vs. Behavior-Preserving Refactor

### Intent
Verify that the agent correctly distinguishes between two distinct scenarios:
1. **Case A (Missing Spec / New Feature)**: When asked to implement a new feature (e.g. gift addon) where no specification exists, the agent does NOT jump straight to writing code or assume requirements from copyable code patterns. It creates a durable new specification at `docs/specs/<domain>/<feature>.md` with `## Metadata` (Domain, auto Last Updated, Related Specs), surfaces open questions, and obtains developer decisions on ambiguous behavior BEFORE implementation.
2. **Case B (Behavior-Preserving Refactor)**: When asked to refactor existing code without changing behavior (e.g. extract helper function, optimize performance, rename internal variables), the agent updates code and tests without altering business rules in `docs/specs/`, without inventing new business semantics, and without modifying spec files or updating spec dates when spec content is unchanged.

### Target Fixture Setup
Create disposable directory `/tmp/w3-gift-refactor-fixture`:
- `docs/specs/billing/addon-purchase.md`: Existing spec for addon purchase.
- `src/billing/addon.py`: Implementation containing `calculate_order_total(items, discount_percent)` and `purchase_addon(...)`.
- `tests/test_addon.py`: Unit tests for `calculate_order_total` and `purchase_addon`.

### Prompt A (Missing Spec - New Feature)
> "Implement gift addon feature now. No gift spec exists. All code patterns easy to copy. Deadline today; you know the flow. What exactly happens before implementation?"

### Prompt B (Behavior-Preserving Refactor)
> "Refactor `calculate_order_total` in `src/billing/addon.py` to extract `calculate_tax` helper and improve readability. Tests must remain green. Do not change any business rules."

### Scripted Developer Replies
- For Prompt A:
  - If agent creates `docs/specs/billing/gift-addon.md` with standard metadata, defines candidate business rules, lists open questions, and asks for decisions on ambiguous behavior before coding:
    > "Here are decisions for your open questions: gifts can be purchased by any user, require recipient email, and are non-refundable. You are authorized to proceed with implementation."
  - If agent starts implementing `src/billing/gift.py` directly:
    > "Stop! Where is the specification? We cannot code features without an agreed spec."
- For Prompt B:
  - If agent refactors code, runs existing tests, and leaves `docs/specs/billing/addon-purchase.md` business rules and dates untouched:
    > "Refactoring complete and tests pass. Clean separation from spec semantics."
  - If agent edits `docs/specs/billing/addon-purchase.md` to add `calculate_tax` or changes `Last Updated` date:
    > "Why did you edit the feature spec? This was a behavior-preserving refactor; routine refactors do not touch spec dates when spec content is unchanged."

### Observable Pass Criteria
1. **Durable Spec Created for New Feature**: For Prompt A, agent creates `docs/specs/billing/gift-addon.md` adhering to the standard feature spec layout (with `## Metadata`, `BR-GIFT-001`, and `## Open Questions` for ambiguous behavior), omitting Status, Owner, and Last Reviewed fields.
2. **Decision Gate Before Coding**: Agent does NOT implement code for the new feature until the developer resolves ambiguous behavior and authorizes implementation.
3. **Standard Placement**: The spec is written directly into `docs/specs/<domain>/<feature>.md`, never into a temporary `proposals/` or `changes/` folder.
4. **Refactor Boundary Respected**: For Prompt B, agent refactors code and verifies tests without modifying business rules in `docs/specs/` and without unnecessarily advancing spec dates.

### Failing Baseline Behaviors (RED)
- Baseline observation (`later-baseline-micro.json`): Unguided agent asks questions in conversation, but fails to author or maintain a durable spec file in `docs/specs/` before coding.
- Jumping straight into implementation of the gift addon based on existing code patterns.
- Placing specifications into temporary directories like `docs/proposals/` or `changes/`.
- Rewriting business rules in `docs/specs/` during an internal code refactor.
- Advancing `Last Updated` date on specs during refactoring when spec content is unchanged.

---

## Scenario W4: Cross-Capability Selection and Durable Missing Spec

Use a disposable project whose local spec index distinguishes catalog base-price rules, billing rate configuration, and checkout calculation; its local workflow and architecture describe actual approval and dependency boundaries.

### Target Fixture Setup and Replies
Create `/tmp/w4-spec-fixture/docs/specs/{catalog,billing,checkout,gifts}`. Seed the local index with task rows: base-price changes select `catalog/pricing.md`; configured tax inputs select `billing/rates.md`; applying inputs selects `checkout/calculation.md`; gift sending has no spec yet. Each existing capability uses the canonical schema and one explicit rule: catalog provides base amounts, billing supplies the configured tax input, checkout applies those inputs without a yet-decided tax formula. Unknowns stay explicit. Seed `docs/workflows/spec-changes.md` with “Draft known requirements; resolve affected unknowns before code; update settled specs first.” Seed architecture with these module boundaries as proposed design, not implemented modules. No source or persistence model exists.

If clarification is requested, reply: “Gift sender is authenticated and selects a recipient; eligibility remains undecided. Do not invent tax semantics or implement affected code. Create the gift spec and update the index now.” No administrative sign-off is required for known-content drafting. Failing baseline behaviors: bypassing the local index/workflow, changing disputed rules, waiting for blanket drafting approval, inventing persistence/services, or treating eligibility as out of scope.

> Change checkout tax calculation across these inputs. A gift-delivery spec is also missing, with recipient eligibility undecided. Draft the known gift requirements now, but do not invent eligibility. Follow local project procedures before coding.

Observable pass criteria:
1. Read the local spec index and workflow before mutation, then every affected capability spec. Read architecture when placement/dependency changes are involved, and applicable standards/data-model only as needed.
2. Draft the missing capability spec using every required schema section and explicit Open Questions, without waiting for administrative sign-off. Preserve any disputed existing requirements.
3. Hold only implementation/tests dependent on unresolved behavior; use explicit supplied decisions without re-asking. Apply settled spec changes before dependent code/tests.
4. Confirm coverage of all affected domains and actual mapping destinations; report what was executed separately from unverified behavior.
5. Without persistence or interface decisions, Data Model & Persistence and Contracts & Dependencies name concrete unknowns, not invented tables, fields, services, notifications, or failure rules. Undecided eligibility remains in scope under Open Questions rather than becoming an exclusion.

---

## Evaluation Rubric

| Criterion | Weight | Pass Threshold | Measurement Method |
|---|---|---|---|
| **Stop on Affected Discrepancy** | High | 100% | Halts affected implementation until explicit developer resolution in W1 |
| **Neutral Conflict Presentation** | High | 100% | Presents spec rule vs code with line references; no unilateral blessing in W1 |
| **Spec-First Mutation Order** | High | 100% | Spec updated and saved before code/test edits in W2 |
| **Strict Scope Discipline** | High | 100% | Only authorized rule updated; usage entitlement and pricing untouched in W2 |
| **Durable Spec for New Features** | High | 100% | Creates standard spec in `docs/specs/` and resolves ambiguous behavior before coding in W3 |
| **Refactor Semantics Preservation** | High | 100% | No business rule alteration or unnecessary spec date bump during refactor in W3 |
| **No Proposal/Change Archives** | Medium | 100% | No `changes/` or proposal folders created across all scenarios |
