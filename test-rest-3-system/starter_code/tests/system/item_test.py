from models.store import StoreModel
from tests.not_unit_base_test import BaseTest
import json


class TestItem(BaseTest):
    def test_add_item(self):
        with self.app() as client:
            with self.app_context:
                client.post('store/Test_Store', data={'name': })