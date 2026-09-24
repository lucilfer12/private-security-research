#!/usr/bin/env python3
"""Deterministic reproduction of the reported bridge derivation collision.

This models the derivation logic in the supplied qorechain-core snippet using
Python's standard-library SHAKE256 implementation. It intentionally uses a
synthetic mnemonic and synthetic addresses; no real private key is generated.
"""

from __future__ import annotations

import hashlib

TEST_MNEMONIC = "audit-only-test-mnemonic-do-not-use"
ADDRESS_A = "qor1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
ADDRESS_B = "qor1bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"


def bridge_seed(mnemonic: str) -> bytes:
    """Reported vulnerable path: SHAKE256(mnemonic), 32 bytes."""
    return hashlib.shake_256(mnemonic.encode()).digest(32)


def adapter_seed(address: str, mnemonic: str) -> bytes:
    """Address-bound reference path from the supplied snippet."""
    material = f"qorechain:pqc:v1|{address}|{mnemonic}".encode()
    return hashlib.shake_256(material).digest(32)


def main() -> None:
    bridge_a = bridge_seed(TEST_MNEMONIC)
    bridge_b = bridge_seed(TEST_MNEMONIC)
    adapter_a = adapter_seed(ADDRESS_A, TEST_MNEMONIC)
    adapter_b = adapter_seed(ADDRESS_B, TEST_MNEMONIC)

    print("Synthetic input only — no real wallet material is used.")
    print(f"bridge A:   {bridge_a.hex()}")
    print(f"bridge B:   {bridge_b.hex()}")
    print(f"bridge eq:  {bridge_a == bridge_b}")
    print(f"adapter A:  {adapter_a.hex()}")
    print(f"adapter B:  {adapter_b.hex()}")
    print(f"adapter eq: {adapter_a == adapter_b}")


if __name__ == "__main__":
    main()
