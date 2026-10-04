import unittest

from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart


class TestItemToPurchase(unittest.TestCase):

    def test_item_creation(self):
        item = ItemToPurchase(
            "Bread",
            2.50,
            3,
            "Loaf of white bread"
        )

        self.assertEqual(item.item_name, "Bread")
        self.assertEqual(item.item_price, 2.50)
        self.assertEqual(item.item_quantity, 3)
        self.assertEqual(item.item_description, "Loaf of white bread")


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart(
            customer_name="DarF",
            current_date="October 4, 2026"
        )

        self.bread = ItemToPurchase(
            "Bread",
            2.50,
            2,
            "Loaf of white bread"
        )

        self.milk = ItemToPurchase(
            "Milk",
            3.00,
            1,
            "One gallon of milk"
        )

    def test_add_item(self):
        result = self.cart.add_item(self.bread)

        self.assertTrue(result)
        self.assertEqual(len(self.cart.cart_items), 1)
        self.assertIs(self.cart.cart_items[0], self.bread)

    def test_add_duplicate_item(self):
        self.cart.add_item(self.bread)

        duplicate = ItemToPurchase(
            "Bread",
            4.00,
            5,
            "Another loaf"
        )

        result = self.cart.add_item(duplicate)

        self.assertFalse(result)
        self.assertEqual(len(self.cart.cart_items), 1)

    def test_remove_item(self):
        self.cart.add_item(self.bread)
        self.cart.add_item(self.milk)

        result = self.cart.remove_item("Bread")

        self.assertTrue(result)
        self.assertEqual(len(self.cart.cart_items), 1)
        self.assertEqual(self.cart.cart_items[0].item_name, "Milk")

    def test_remove_missing_item(self):
        self.cart.add_item(self.bread)

        result = self.cart.remove_item("Eggs")

        self.assertFalse(result)
        self.assertEqual(len(self.cart.cart_items), 1)

    def test_modify_item(self):
        self.cart.add_item(self.bread)

        modified_item = ItemToPurchase(
            "Bread",
            2.50,
            5,
            "Loaf of white bread"
        )

        result = self.cart.modify_item(modified_item)

        self.assertTrue(result)
        self.assertEqual(self.cart.cart_items[0].item_quantity, 5)
        self.assertEqual(self.cart.cart_items[0].item_price, 2.50)

    def test_modify_missing_item(self):
        modified_item = ItemToPurchase(
            "Eggs",
            4.00,
            12,
            "One dozen eggs"
        )

        result = self.cart.modify_item(modified_item)

        self.assertFalse(result)
        self.assertEqual(len(self.cart.cart_items), 0)

    def test_get_num_items(self):
        self.cart.add_item(self.bread)
        self.cart.add_item(self.milk)

        self.assertEqual(self.cart.get_num_items(), 3)

    def test_get_cost_of_cart(self):
        self.cart.add_item(self.bread)
        self.cart.add_item(self.milk)

        # Bread: $2.50 x 2 = $5.00
        # Milk:  $3.00 x 1 = $3.00
        # Total: $8.00
        self.assertEqual(self.cart.get_cost_of_cart(), 8.00)

    def test_get_item_byname(self):
        self.cart.add_item(self.bread)

        result = self.cart.get_item_byname("bread")

        self.assertIs(result, self.bread)

    def test_get_item_byname_missing(self):
        self.cart.add_item(self.bread)

        result = self.cart.get_item_byname("Eggs")

        self.assertFalse(result)

    def test_multiple_items(self):
        self.cart.add_item(self.bread)
        self.cart.add_item(self.milk)

        self.assertEqual(len(self.cart.cart_items), 2)
        self.assertEqual(self.cart.get_num_items(), 3)
        self.assertEqual(self.cart.get_cost_of_cart(), 8.00)

    def test_item_description(self):
        self.cart.add_item(self.bread)

        self.assertEqual(
            self.cart.cart_items[0].item_description,
            "Loaf of white bread"
        )


if __name__ == "__main__":
    unittest.main()
