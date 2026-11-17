# Skill Invocation and Project Specs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Make four project-knowledge skills manually invoked and keep project specifications aligned with new and changed features.

**Architecture:** Use the host's supported manual-invocation mechanism for the four skills. Retain automatic discovery for `working-with-project-specs`, narrowing its trigger to work governed by project specifications and clarifying its spec-first feature workflow.

**Tech Stack:** Markdown skill frontmatter, project knowledge references, SkillEvaluator.

**Spec:** Approved short design in the conversation on 2026-11-17: manual invocation for four skills, automatic spec-context routing for `working-with-project-specs`, and spec-first documentation for new and changed features.

## Global Constraints

- Preserve existing specification conflict and unresolved-behavior safeguards.
- Do not require a separate specification for helpers or internal changes that do not change a feature's behavior.
- Do not claim manual-only behavior on a runtime unless its actual skill loader supports it.
- Retain existing shared authoring and specification standards as the authoritative formats.

## Review Focus

- A runtime that ignores `disable-model-invocation`: identify the limitation rather than claiming enforcement.
- A new feature with partially unspecified behavior: document known facts and block only dependent work.
- An authorized feature change: update its existing spec before dependent code.
- A behavior-preserving refactor: retain rules and update mappings only when their targets move.
- A read-only code exploration: do not route it through the implementation workflow solely because code is inspected.

### Task 1: Establish supported invocation control and update skills

**Files:**
- Modify: `skills/auditing-project-knowledge/SKILL.md`
- Modify: `skills/documenting-existing-projects/SKILL.md`
- Modify: `skills/initializing-project-knowledge/SKILL.md`
- Modify: `skills/structuring-project-documentation/SKILL.md`
- Modify: `skills/working-with-project-specs/SKILL.md`
- Modify: `README.md`

- [ ] Inspect the actual installed skill loader's documented or implemented frontmatter handling for `disable-model-invocation`; distinguish support in each relevant host. Record concrete evidence and limitations in the final report. Do not install tooling to establish support without approval.
- [ ] Add `disable-model-invocation: true` to the four manual skills, preserving their names and bodies. Make descriptions concise human-facing summaries. Leave `working-with-project-specs` model-invocable.
- [ ] Adjust the automatic skill's description and task routing so code inspection alone does not activate its implementation workflow. Preserve the condition that the repository has project specifications or standards.
- [ ] Clarify spec-first handling: create the feature spec for new features; update the affected existing spec for changed feature behavior; use supplied decisions, document unknowns, and block only work that depends on unresolved behavior. Keep existing conflict safeguards, shared authoring references, and refactor mapping behavior.
- [ ] Update `README.md` invocation guidance and examples to name the four manual skills explicitly, accurately explaining any runtime-specific limitation discovered above.
- [ ] Run the narrowest existing reference synchronization check identified from `scripts/sync-references.py` and relevant tests. Run keyless `skillevaluator quality-check` on the five changed skill directories; capture exit codes and findings. Do not install scanners or call paid providers without permission.
- [ ] Verify the five review-focus scenarios against the resulting instructions, distinguishing textual review from observed runtime behavior. Report what could not be demonstrated.
