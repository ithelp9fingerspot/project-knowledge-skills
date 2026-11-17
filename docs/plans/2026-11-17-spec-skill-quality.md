# Project Specs Skill Quality Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan inline. Steps use checkbox syntax for tracking.

**Goal:** Improve the usefulness and static quality of `working-with-project-specs` without weakening its specification safeguards.

**Architecture:** Keep the current skill and shared references authoritative. Address demonstrated missing-reference gaps and add concise task examples; do not add invented metadata or filler solely to satisfy a score.

**Tech Stack:** Markdown, SkillEvaluator quality-check, existing reference sync checker.

**Spec:** Approved short design in the conversation on 2026-11-17; Tier 3 explicitly excluded.

## Global Constraints

- New features and authorized behavior changes remain spec-first.
- Preserve conflict handling, unresolved behavior gates, and behavior-preserving refactor rules.
- Do not claim improvement of live agent behavior from static grading.
- Do not run Tier 3 or call paid providers.

## Review Focus

- Missing project spec index must not be treated as evidence that a spec does not exist.
- Inaccessible authoritative material must not be replaced by invented rules.
- A missing bundled authoring reference must not be silently replaced by a partial format.
- An approved change to a disputed rule must preserve unrelated rules.
- An unresolved rule must block only behavior depending on that rule.

### Task 1: Improve the skill and evaluate it

**Files:** `skills/working-with-project-specs/SKILL.md`; inspect linked shared authoring references without changing their ownership.

- [ ] Inspect current missing-document and nested-reference handling and record a baseline scenario for the missing-reference path.
- [ ] Add only necessary missing/inaccessible-document handling; keep project-local absences distinct from missing bundled authoring requirements.
- [ ] Add concise realistic examples for a new feature and an authorized change, preserving the handling of unknown behavior.
- [ ] Leave metadata unset when its value is unknown, and preserve nested references that provide necessary single-source guidance.
- [ ] Run `python3 scripts/sync-references.py --check` and `skillevaluator quality-check skills/working-with-project-specs`; capture exit codes and compare with the previous 85.8/B result.
- [ ] Check the five review-focus scenarios against the changed instructions and report static-evaluation limitations.
