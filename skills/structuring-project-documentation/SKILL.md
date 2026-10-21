---
name: structuring-project-documentation
description: Use when scaffolding documentation formats without implementation discovery, or reorganizing selected existing docs into a standard structure without validating them against code
---

# Structuring Project Documentation

Create a navigable documentation framework, not an investigated knowledge base. Existing docs can supply headings or selected content; source reuse does not validate their claims.

## Scope

Use this workflow for empty outlines and docs-based restructuring, whether application code exists or not. Content discovery from implementation belongs to `documenting-existing-projects`; requirements-based authoring belongs to `initializing-project-knowledge`; code/doc alignment checks belong to `auditing-project-knowledge`. Those skills are alternative workflows, not installation dependencies.

## Workflow

1. **Bound the task.** Inventory destination filenames and required repository instructions. Read the [structuring contract](references/project-knowledge-standard.md#documentation-structuring) and [naming convention](references/project-knowledge-standard.md#file-naming). Determine files requested, allowed source sections, and source depth. Explicit requests settle those choices; otherwise default to outline-only and create-missing. If sources are requested but unnamed, ask which sources may be inspected. **Done:** every input has a permitted reading depth and every destination has a write boundary.

2. **Map the structure.** Outline-only reads selected headings; selected-content reuse reads complete selected sections. Read only the affected document recipes in the [authoring guide](references/project-knowledge-authoring.md). Recipe headings govern the output; legacy headings help place topics within them. Disclose creations, collisions, and authorized updates. Under create-missing, skip existing destinations and proceed with missing ones; ask about a collision only when updating that file is requested. **Done:** every scoped file has a recipe, source mapping or filling plan, and any mutation of existing content is authorized.

3. **Write the framework.** Apply the shared contract's outline notice, English filling prompts, attribution, and conditional sections. Use actual links and label outline targets. For `AGENTS.md`, provide task-conditioned routes and the incomplete-guidance boundary; for `CLAUDE.md`, use its exact [entrypoint recipe](references/project-knowledge-authoring.md#claudemd). Keep material behind ordinary task pointers; the Claude entrypoint alone imports eagerly. **Done:** every authorized destination has its applicable headings; each reused passage preserves source meaning and caveats; no inferred project policy fills a gap.

4. **Verify the deliverable.** Follow generated links and import targets; compare preserved files with their starting byte digests. Digest reads verify preservation without interpreting out-of-scope content. For authorized rewrites, account for every affected source passage, including unique operational instructions. Report created/updated/preserved files, outlines versus reused content, decisions still needed, and that implementation alignment was not checked. **Done:** the shared structuring completion criteria hold; structural checks are distinguished from runtime loading or business validation.

## Example

“Use only `docs/legacy.md#local-setup` as content for `docs/development.md`; leave other sections as filling prompts and preserve the source.” Read that section, retain its commands with source attribution and an unvalidated-content note, then create only authorized missing destinations. Application code and unrelated legacy policy remain outside this task.
