# Reproduction

Run:

```bash
python3 -m unittest discover -s poc -p 'test_*.py'
python3 poc/reproduce.py
```

Expected properties:

- The reported `bridge` derivation produces the same 32-byte seed for the same mnemonic regardless of account/address identity because the address is not an input to the function.
- The `adapter` reference path changes the seed when the address changes.

This is a deterministic derivation-level reproduction. It does **not** generate a production ML-DSA/Dilithium keypair and does not interact with QoreChain or any live service.
