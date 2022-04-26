from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def setUp(self):
        pass

    def test_create_item(self):
        item = ItemModel("Test", 20)

        self.assertEqual("Test", item.name, "Name of item after creation does not equal constructor argument")
        self.assertEqual(20, item.price, "Price of item after creation does not equal constructor argument")
        self.assertIsNotNone(item)

    def test_json(self):
        item = ItemModel("Test", 20)
        expected = {
            "name": "Test",
            "price": 20
        }
        self.assertDictEqual(expected, item.json())
