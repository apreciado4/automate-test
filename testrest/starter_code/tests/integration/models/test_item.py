from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context:
            item = ItemModel("Test", 20)

            self.assertIsNone(ItemModel.find_by_name("Test"), f"Found and item with name {item.name}, but expected not to")
            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name("Test"), f"Item with name {item.name} is not found")
            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name("Test"), f"Found an item with namr {item.name}, but expected not to")