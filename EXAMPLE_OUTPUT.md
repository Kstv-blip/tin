# Activation Rescue Brief

## Trigger
Weekly activation review for the supplied signup cohort. The run uses `activation` as the activation event and a 7-day activation window.

## Data scope
6 signup records were supplied. All 6 had enough signup/activation timing data to evaluate activation within the window. Overall activation was 3/6 (50%).

## Diagnosed leak
The paid acquisition cohort is the clearest actionable leak in this sample: 1 of 3 paid signups activated within 7 days (33.3%), versus 2 of 3 organic signups (66.7%).

This is a small sample, so the difference is directional rather than a reliable estimate of a persistent channel effect.

## Target audience
Users who:
- entered through `acquisition_source = paid`;
- signed up within the review cohort;
- have not completed the `activation` event within 7 days of signup.

## One rescue campaign
**Channel:** Email, assuming email is available for these users.

**Timing:** Trigger when a paid signup reaches the 7-day non-activation point.

**Message angle:** Remove the likely final-step friction by pointing the user directly to the activation action, rather than describing the full product.

**CTA:** Complete the activation action.

**Optional sequence:** If the campaign supports multiple touches, use one immediate activation nudge at day 7 and one final help-oriented reminder 2–3 days later. Stop the campaign as soon as activation occurs.

## Measurement
**Primary metric:** 7-day activation rate for the targeted paid-signup cohort.

**Guardrail:** Unsubscribe/complaint rate, monitored against the campaign's existing baseline.

**Comparison:** Compare against the equivalent paid-signup cohort before the campaign, using the same activation definition and 7-day window.

## Why this action
**Observed:** The supplied sample shows lower activation among paid signups than organic signups.

**Inferred:** Paid-acquired users may need a clearer path to first value, or the acquisition promise may be attracting a cohort with different activation needs. The supplied data does not establish the cause.

**Proposed:** Test a targeted activation nudge against the paid non-activated cohort instead of changing the whole onboarding experience.

## Missing evidence / assumptions
- The sample is too small to establish a durable channel-level difference.
- No email delivery data or existing campaign history was supplied.
- No event-level sequence beyond the last event was supplied, so the campaign should not claim a specific product friction as proven.
