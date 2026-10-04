class ItemToPurchase:
    def __init__(
        self,
        item_name="none",
        item_price=0.0,
        item_quantity=0,
        item_description="none"
    ):

	# Note: Intro level class, assuming valid values passed
        # Production code would re-validate inputs
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} "
            f"@ ${self.item_price:.2f} = ${item_total:.2f}"
        )
