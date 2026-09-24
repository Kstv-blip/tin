# Add growth.activation_rescue workflow

## What it does

`growth.activation_rescue` turns a supplied signup cohort and activation definition into one evidence-backed lifecycle campaign brief.

It:
1. validates the activation measurement contract;
2. computes the cohort's activation behavior;
3. identifies one actionable activation leak;
4. defines one reproducible audience;
5. proposes one rescue campaign with timing, message angle and CTA;
6. defines a success metric and guardrail.

The workflow writes one project artifact: `reports/ACTIVATION_RESCUE.md`.

## Who would run it

A founder or growth operator should run it when a signup cohort is under-activating, after a product/onboarding change, or on a recurring weekly review.

## Why this is missing today

Tin already covers acquisition/organic growth, content, cold outreach, product QA, and several adjacent growth analyses. The current public roadmap also calls out lifecycle marketing as an area to build out.

The checked open PR list on September 24, 2026 includes several new growth workflows, but not a workflow that starts with an activation leak and ends with one targeted rescue campaign. The package deliberately avoids overlapping with competitor, landing-page, directory, churn-reason, sales-objection and audience-prospector work visible in those PRs.

## How it works

The founder supplies a project-relative CSV containing signup and activation evidence plus the one event that defines activation. The procedure is deliberately evidence-first: it refuses to invent missing analytics, calculates the activation window, inspects available segments, selects one actionable leak, and turns it into one campaign brief.

The campaign can be a single touch or a short sequence of up to three touches, but it remains one intervention concept. No messages are sent and no product files are modified.

## Why the process is useful

Activation work often fails by jumping from a low activation metric directly to generic onboarding advice. This workflow inserts a diagnosis gate: the campaign must be tied to an observed cohort/behavior pattern before the agent proposes an intervention.

## Idea source

The process is informed by Amplitude's activation/cohort analysis guidance and Customer.io's segment-triggered onboarding and activation campaign patterns. The Tin-specific contribution is the bounded diagnostic-to-campaign workflow and its evidence/inference/proposal separation.

## Testing

Offline package-contract tests are included in `tests/test_growth_activation_rescue.py`.

The full Tin community validator and a live/private Tin run still need to be executed from a networked Tin checkout. This submission environment could not clone GitHub, so no claim is made that `uv run tin-lite validate-community` or a live workflow run has passed here.
