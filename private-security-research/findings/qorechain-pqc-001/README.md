# QORECHAIN-PQC-001 — Bridge PQC Seed Derivation Has No Address Binding

## Summary

The supplied `qorechain-core` v3.1.86 snippet shows two derivation families in `x/pqc/client/cli/hybrid_sign.go`:

```go
func deriveDilithiumSeed(derivation, address, mnemonic string) ([]byte, error) {
    switch derivation {
    case "bridge", "mnemonic-only":
        return qpqc.Shake256([]byte(mnemonic), 32), nil
    case "adapter", "":
        return qpqc.Shake256([]byte("qorechain:pqc:v1|"+address+"|"+mnemonic), 32), nil
    default:
        return nil, fmt.Errorf("unknown derivation %q (use adapter|bridge)", derivation)
    }
}
```

Under the reported `bridge` / `mnemonic-only` path, the derived seed depends only on the mnemonic. The `address` parameter is not incorporated, so multiple accounts that intentionally share the same mnemonic receive the same PQC seed material.

## Security invariant

Distinct accounts derived from one HD-wallet mnemonic should not unintentionally share the same PQC signing key unless that sharing is an explicit, documented design decision.

## Reachability

The issue matters when the `bridge` or `mnemonic-only` path is actually selected and more than one account is derived from the same mnemonic. The supplied code comments reportedly associate this mode with production-oriented bridge/faucet/dashboard components; those deployment claims should be independently verified before being treated as established fact.

## Reproduction

The local PoC calls the equivalent SHAKE256 construction with:

- one synthetic test mnemonic;
- two synthetic addresses;
- 32-byte SHAKE256 output.

The two `bridge` calls produce an identical digest. The address-bound `adapter` construction produces different digests for the two addresses.

### Deterministic sample output

```text
bridge seed: 65680db0e7b343a93203d5f65e7fb4972888a7ee7bef76c15708fb136f1117d5
adapter A:   672893f11b12184f23d9bf6dbeeb64a657386e331a4cd88d79f13eeb13bb8b9b
adapter B:   1c0d930ad5f9dfb16c67f64c4ae5e8e05e05e7c21e4da3c96287dc71801b4dfe
```

The sample values are only regression-test material and are not wallet credentials.

## Impact model

### Directly demonstrated

The derivation function, as supplied, creates identical seed bytes for the same mnemonic on the `bridge` path. A deterministic key-generation pipeline that consumes those bytes will therefore start from the same seed material.

### Deployment-dependent

Practical cross-account signature forgery requires that multiple security principals actually use colliding PQC keys and that an attacker obtain one corresponding private key. Whether this can occur in a production deployment depends on account derivation, key storage, service architecture, signing flows, and verification rules.

The impact should therefore be described as a **cryptographic key-isolation failure in the derivation path**, with any stronger production consequence tied to independently verified deployment facts.

## Remediation

Prefer removing the ambiguous `bridge` / `mnemonic-only` mode, or make the derivation explicitly account-bound by mixing a stable account identifier (for example an address or explicit derivation index) into domain-separated input.

Any already-created keys under the colliding derivation need coordinated rotation once the implementation is changed, because changing the derivation formula does not retroactively change existing private keys.

## Validation status

**Current status:** static reproduction of the supplied function logic.

**Not independently verified in this repository:**

- exact upstream source revision for v3.1.86;
- which production deployments select `bridge`;
- whether affected services derive more than one account from the same mnemonic;
- whether any real deployment has already exposed a corresponding PQC private key.

## Ethics and scope

This case study is for authorized security research and private assessment reporting. The PoC uses synthetic values only and performs no network calls.
