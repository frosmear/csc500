import unittest
from module6 import ItemToPurchase, ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        """Create a fresh cart before each test."""
        self.cart = ShoppingCart(
            customer_name="Test Customer",
            current_date="August 29, 2026"
        )

        self.apple = ItemToPurchase("Apple", 1.50, 3)
        self.banana = ItemToPurchase("Banana", 0.75, 4)

    # ------------------------------------------------------------
    # Required Core Method Tests
    # ------------------------------------------------------------

    def test_add_item(self):
        result = self.cart.add_item(self.apple)

        self.assertTrue(result)
        self.assertEqual(len(self.cart.cart_items), 1)
        self.assertIs(self.cart.cart_items[0], self.apple)

    def test_remove_item(self):
        self.cart.add_item(self.apple)

        result = self.cart.remove_item("Apple")

        self.assertTrue(result)
        self.assertEqual(len(self.cart.cart_items), 0)

    def test_remove_item_case_insensitive(self):
        self.cart.add_item(self.apple)

        result = self.cart.remove_item("APPLE")

        self.assertTrue(result)
        self.assertEqual(len(self.cart.cart_items), 0)

    def test_remove_item_not_found(self):
        self.cart.add_item(self.apple)

        result = self.cart.remove_item("Orange")

        self.assertFalse(result)
        self.assertEqual(len(self.cart.cart_items), 1)

    def test_remove_multiple_matching_items(self):
        self.cart.add_item(ItemToPurchase("Apple", 1.50, 3))
        self.cart.add_item(ItemToPurchase("APPLE", 2.00, 5))
        self.cart.add_item(ItemToPurchase("Banana", 0.75, 4))

        result = self.cart.remove_item("apple")

        self.assertTrue(result)
        self.assertEqual(len(self.cart.cart_items), 1)
        self.assertEqual(
            self.cart.cart_items[0].item_name,
            "Banana"
        )

    def test_modify_item(self):
        self.cart.add_item(self.apple)

        modified = ItemToPurchase("Apple", 2.00, 10)

        result = self.cart.modify_item(modified)

        self.assertTrue(result)

        item = self.cart.get_item_byname("apple")

        self.assertEqual(item.item_price, 2.00)
        self.assertEqual(item.item_quantity, 10)

    def test_modify_item_not_found(self):
        self.cart.add_item(self.apple)

        modified = ItemToPurchase("Orange", 2.00, 10)

        result = self.cart.modify_item(modified)

        self.assertFalse(result)
        self.assertEqual(len(self.cart.cart_items), 1)

    def test_get_num_items_in_cart(self):
        self.cart.add_item(self.apple)
        self.cart.add_item(self.banana)

        result = self.cart.get_num_items_in_cart()

        self.assertEqual(result, 7)

    def test_get_cost_of_cart(self):
        self.cart.add_item(self.apple)
        self.cart.add_item(self.banana)

        result = self.cart.get_cost_of_cart()

        # Apple: 1.50 * 3 = 4.50
        # Banana: .75 * 4 = 3.00
        # Total: 7.50
        self.assertAlmostEqual(result, 7.50)

    # ------------------------------------------------------------
    # Utility Method Tests
    # ------------------------------------------------------------

    def test_is_incart_with_string(self):
        self.cart.add_item(self.apple)

        self.assertTrue(self.cart.is_incart("Apple"))
        self.assertTrue(self.cart.is_incart("apple"))
        self.assertTrue(self.cart.is_incart("APPLE"))

    def test_is_incart_with_item_object(self):
        self.cart.add_item(self.apple)

        search_item = ItemToPurchase("APPLE", 99.99, 99)

        self.assertTrue(self.cart.is_incart(search_item))

    def test_is_incart_not_found(self):
        self.cart.add_item(self.apple)

        self.assertFalse(self.cart.is_incart("Orange"))

    def test_is_incart_invalid_type(self):
        self.cart.add_item(self.apple)

        self.assertFalse(self.cart.is_incart(12345))

    def test_get_item_byname_with_string(self):
        self.cart.add_item(self.apple)

        result = self.cart.get_item_byname("APPLE")

        self.assertIsInstance(result, ItemToPurchase)
        self.assertIs(result, self.apple)

    def test_get_item_byname_with_object(self):
        self.cart.add_item(self.apple)

        search_item = ItemToPurchase("apple", 99.99, 99)

        result = self.cart.get_item_byname(search_item)

        self.assertIs(result, self.apple)

    def test_get_item_byname_not_found(self):
        self.cart.add_item(self.apple)

        result = self.cart.get_item_byname("Orange")

        self.assertFalse(result)

    def test_get_item_byname_invalid_type(self):
        result = self.cart.get_item_byname(12345)

        self.assertFalse(result)

    # ------------------------------------------------------------
    # Default Attribute Tests
    # ------------------------------------------------------------

    def test_default_values(self):
        cart = ShoppingCart()

        self.assertEqual(cart.customer_name, "none")
        self.assertEqual(cart.current_date, "January 1, 2020")
        self.assertEqual(cart.cart_items, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
