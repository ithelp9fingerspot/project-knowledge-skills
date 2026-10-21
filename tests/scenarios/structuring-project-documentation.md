# Behavioral Scenarios: Structuring Project Documentation

Run each scenario in a fresh disposable directory and fresh agent context. For standalone verification, copy only `skills/structuring-project-documentation/` including its two bundled references outside this repository. Record reads, writes, questions, and final files. Snapshot pre-existing bytes before execution. A generic agent following the import pointer proves traversal, not native Claude loading.

## S1: Format Only Without Project Decisions

**Setup:** Empty repository. No requirements, stack, persistence, or application files.

**Request:** Create the standard documentation framework with headings and short filling instructions only. Do not investigate implementation or gather business requirements.

**Pass:** Creates the seven default entrypoint/core documents. Content outlines use applicable recipe headings, English filling prompts, and the incomplete-content notice. AGENTS has working task routes with outline targets labelled and guards against treating them as confirmed behavior. CLAUDE matches the standard's exact import recipe. All links/imports resolve. No application code, commands, schemas, conditional UI/data-model files, or invented feature specs appear. Reports that implementation alignment was not checked.

**Baseline observed:** The old initializer created no documents: its blank-template ban, requirement gathering, and relative-link CLAUDE contract conflicted with the request.

## S2: Reuse One Legacy Section

**Setup:** `docs/legacy.md` contains Local Setup (`Run make sandbox`), Billing Policy (seven-day cancellation), and Incident Contacts. Add application code and unrelated operational docs as out-of-scope canaries.

**Request:** Use only Local Setup as source content for `docs/development.md`; all other required sections are filling prompts. Create AGENTS and CLAUDE if missing. Preserve all existing files. No code discovery or business-rule validation.

**Pass:** Reads selected setup content completely and only necessary recipes/instructions; source and unrelated files retain their bytes. The setup command is preserved with source section and an implementation-unvalidated note. Billing policy does not become a spec or open behavioral question. Other required development sections remain prompts; unsupported conditional sections are omitted. Navigation and import targets resolve. No script/test invocation validates the legacy command. Report distinguishes copied source claims from verified operational facts.

**Baseline observed:** The existing-project authoring skill read the permitted setup section but produced no destinations because filling prompts and the requested Claude import conflicted with its template and entrypoint rules.

## S3: Outline-Only With Existing Destination Collision

**Setup:** Existing `docs/development.md` contains unique deployment instructions; `docs/legacy.md` has setup and billing headings. Existing CLAUDE includes unique agent guidance. Snapshot all files.

**Request:** Use legacy headings only as a basis for documentation formats. Create missing destinations, preserve sources and existing outputs. Do not read legacy prose for business meaning.

**Pass:** Reads only selected headings for source discovery, plus host-required agent instructions. Existing development and CLAUDE remain byte-identical; missing independent outputs may proceed. Reports collisions without silently converting the existing CLAUDE or overwriting unique notes. No legacy business claims are copied. No validation/audit is claimed. If rewrite is subsequently authorized, reads the complete affected content, accounts for unique notes, and obtains authorization for their destination before replacement. A whole-file replacement requires a whole-file read.

## S4: Authorized Merge of Oversized Agent Instructions

**Setup:** Existing AGENTS has 184 physical lines under legacy headings, including a deployment freeze requiring incident-commander consent, a task-specific deployment runbook, and redundant navigation. Existing architecture and development documents have recipe headings; an unrelated compliance note is a preservation canary. Snapshot all files.

**Request:** Merge AGENTS into the current format. Reading existing instructions and updating AGENTS plus development to relocate its deployment runbook are authorized; preserve unique meaning and unrelated files. Use existing docs as source only; no implementation discovery.

**Pass:** Final AGENTS uses Scope, Task Routing, Approval Boundaries, Completion in order, with live task-conditioned links and at most 150 physical lines, targeting 60–100 without padding or minification. The deployment-consent rule remains operative; the runbook remains intact in development and is reached from AGENTS. No legacy-format appendix or dropped instruction substitutes for normalization. Reports actual line count and relocated content. Unrelated bytes remain unchanged; code alignment is not claimed.

**Boundary variant:** Authorize AGENTS edits only. If preserving unique content requires another destination, request scoped relocation permission instead of deleting content or delivering more than 150 lines as compliant.

**Lossless merge check:** Include a cryptographically signed Incident Commander approval-token requirement, end-to-end tests in ephemeral containers, warning-free linting, semver release tags, and distinct internal reference URLs in the legacy fixture. Every unique rule, qualifier, command, URL, and runbook step must remain reachable with equivalent force after merging; line-count success alone is a failure if any disappear.

**Observed first smoke failure:** The merge reduced 184 lines to 62 with valid routes but dropped approval-token, verification, release-tag, and reference details. Require source-item accounting and verify final content, not just headings and size.

## S5: Partially Filled Documents Must Not Masquerade as Project Knowledge

**Setup:** Only a source Local Setup section (`Run make sandbox`) is available. Other development requirements are unknown.

**Request:** Reuse that section in development and scaffold the missing required sections. Generate agent routing and a docs index; preserve the source. No command execution or implementation validation.

**Pass:** Development begins with the incomplete-document notice and action-required notice from the standard. Local Setup retains its source and implementation-unvalidated caveat; every unfinished section says `Needs project input:` and names the missing facts. Both AGENTS routes and the docs index label development `incomplete outline`. AGENTS explicitly prevents filling prompts/examples/unvalidated instructions from becoming authoritative requirements or executable procedures; independent confirmed work remains possible. CLAUDE stays exactly `@AGENTS.md`. Delivery lists unfinished files and required inputs rather than claiming a completed knowledge base.

**Fail:** A bare template without visible warnings; fake stack/commands/policies filling gaps; a warning only in the final chat; or removing the top warning after filling just Local Setup.
