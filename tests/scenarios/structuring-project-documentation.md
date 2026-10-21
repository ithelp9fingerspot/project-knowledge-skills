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
