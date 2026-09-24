---
name: activation-rescue
description: Diagnose one activation drop-off from a signup cohort and turn it into one targeted lifecycle campaign brief.
---

# Activation rescue method

## 1. Establish the measurement contract
- Read the supplied CSV and inspect its columns before analyzing it.
- Treat `activation_event` as the only activation definition for this run.
- Treat activation as successful only when the event occurs within `activation_window_days` after signup.
- If the file does not contain enough information to determine signup and activation timing, stop with a missing-evidence report.
- Never silently substitute a different activation event.

## 2. Build the cohort
- Determine the usable signup population from the supplied rows.
- Exclude rows that cannot be evaluated and report how many were excluded and why.
- If the data contains acquisition source, plan, persona, or other segmentation fields, use them only when populated and relevant.
- Do not infer demographics, intent, or company attributes that are not in the data.

## 3. Find the leak
Calculate the overall activation rate where possible.
Then inspect available behavioral segments and timing patterns to find ONE segment or stage with a meaningful, actionable gap.
Prefer a segment when:
- it has enough observations to avoid a one-user anecdote;
- its activation rate differs materially from the cohort baseline;
- the difference points to a plausible intervention;
- the segment is addressable by a marketing message.

If multiple candidates are plausible, choose the one with the clearest evidence and explain the tie-breaker. Do not rank several recommendations.

## 4. Design the rescue campaign
The campaign must target the diagnosed segment and move users toward the defined activation event.

Specify:
- Audience rule: fields/conditions a founder could reproduce in their lifecycle tool.
- Channel: choose from channels supported by the evidence or explicitly state that the channel is a proposed assumption.
- Timing: based on the observed time-to-activation or inactivity pattern when available.
- Message angle: address the strongest evidenced friction or missing step.
- CTA: one low-friction action that directly advances toward activation.

Keep the campaign to one intervention concept. If a sequence is useful, it is one campaign with up to three touches, not three separate recommendations.

## 5. Measurement
Define:
- Primary success metric: activation rate within the same window, or time-to-activation if the data supports it.
- Guardrail: unsubscribe/complaint rate, spam rate, or another relevant negative signal if available. Do not invent a baseline.
- Suggested observation window and comparison cohort.

## 6. Evidence discipline
Separate:
- Observed: directly computed or read from the CSV.
- Inferred: a reasonable interpretation of the observed behavior.
- Proposed: the campaign decision.

Never claim the campaign will improve activation. The report is a testable intervention, not an outcome guarantee.

## Output
Write `reports/ACTIVATION_RESCUE.md` with these headings:

# Activation Rescue Brief
## Trigger
## Data scope
## Diagnosed leak
## Target audience
## One rescue campaign
## Measurement
## Why this action
## Missing evidence / assumptions

The report must be concise enough for a founder to act on immediately.