# Security Research Methodology

## 1. Understand the state machine
Map storage variables, transitions, privileged actors, external calls, and failure paths.

## 2. Write the invariant
State the security property that must always hold.

## 3. Prove reachability
Verify deployment, initialization, configuration, roles, and the exact state needed for the finding.

## 4. Prove exploitability
Identify the concrete caller, preconditions, attacker-controlled input, and resulting security boundary crossing.

## 5. Quantify impact
Separate direct cryptographic or financial impact from assumptions required to reach it.

## 6. Reproduce locally
Prefer deterministic, minimal tests that use synthetic data.

## 7. Add a regression test
Encode the intended invariant so future changes cannot silently reintroduce the issue.

## 8. Respect scope
A technically valid pattern can still be irrelevant when a component is inactive, unreachable, unconfigured, fixed in the deployed version, or outside an authorized assessment scope.
