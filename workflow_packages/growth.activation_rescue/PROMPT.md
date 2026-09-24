Read the project context and the supplied signup cohort CSV. Follow the activation-rescue skill.

Goal: turn behavioral evidence into exactly ONE concrete marketing action a founder can review and execute next.

Inputs:
- cohort_file: project-relative CSV path supplied by the founder
- activation_event: the single event that represents first meaningful value
- activation_window_days: the maximum time after signup in which activation counts
- trigger_context: optional reason for running this workflow

Write only reports/ACTIVATION_RESCUE.md.

Do not send messages, modify the product, edit source files, contact customers, or invent missing analytics. If the supplied data cannot support a defensible activation diagnosis, explain the missing evidence in the report and stop rather than manufacturing a campaign.

The report must contain:
1. Run trigger and data scope.
2. One diagnosed activation leak, supported by counts/rates or explicit evidence from the supplied data.
3. One target audience definition that can be turned into a segment.
4. One rescue intervention, including channel, timing, core message angle, and CTA.
5. One success metric and one guardrail.
6. A short "Why this action" section distinguishing evidence from inference.

Do not produce a list of five tactics. The output is one campaign brief.