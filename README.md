# Private Security Research

A reproducible research workspace for authorized security assessments, focused experiments, proof-of-concept demonstrations, and regression tests.

## Research model

**Code pattern → Reachability → Exploitability → Impact → Reproducibility**

A dangerous-looking pattern is not automatically a practical vulnerability. Each case separates the vulnerable mechanism from deployment assumptions, privilege requirements, reachable state, and measurable impact.

## Repository structure

```text
findings/     Technical case studies and evidence
poc/          Small, deterministic reproductions
docs/         Methodology and threat modeling
templates/    Reusable templates for future assessments
```

## Scope and disclosure

This repository is intended for **authorized private security assessments and research**. Do not use the included techniques against systems you are not authorized to test.

Client-sensitive material should be redacted before publication. Never commit credentials, seed phrases, private keys, API tokens, production addresses when they are not necessary, or unreleased internal documents.

## Current case study

- `QORECHAIN-PQC-001` — Bridge PQC key derivation lacks account/address binding in the supplied `qorechain-core` v3.1.86 snippet.

The current reproduction uses a synthetic test mnemonic and synthetic addresses. It does not derive or publish a real Dilithium/ML-DSA private key.

## Validation status

The QoreChain case currently documents a **static reproduction of the supplied code path**. Upstream commit/version provenance, deployment configuration, and production exposure should be recorded separately when independently verified.
