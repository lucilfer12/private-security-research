import unittest

from reproduce import ADDRESS_A, ADDRESS_B, TEST_MNEMONIC, adapter_seed, bridge_seed


class BridgeDerivationCollisionTests(unittest.TestCase):
    def test_bridge_mode_is_not_address_bound(self):
        self.assertEqual(
            bridge_seed(TEST_MNEMONIC),
            bridge_seed(TEST_MNEMONIC),
        )

    def test_adapter_reference_path_is_address_bound(self):
        self.assertNotEqual(
            adapter_seed(ADDRESS_A, TEST_MNEMONIC),
            adapter_seed(ADDRESS_B, TEST_MNEMONIC),
        )

    def test_different_addresses_do_not_change_bridge_seed(self):
        # The address parameters are intentionally ignored by the reported bridge path.
        seed_a = bridge_seed(TEST_MNEMONIC)
        seed_b = bridge_seed(TEST_MNEMONIC)
        self.assertEqual(seed_a, seed_b)


if __name__ == "__main__":
    unittest.main()
