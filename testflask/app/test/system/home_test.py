from test_base import BaseTest
import json


class TestHome(BaseTest):
    # Do Not Touch
    # def test_home_original(self):
    #     with app.app.test_client() as c:
    #         resp = c.get('/')
    #
    #         # For all web requests 200 means OK, 404 not found, 500 internal server error
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertEqual(json.loads(resp.get_data()),
    #                          {'message': 'Hello World'})

    def test_home(self):
        with self.app() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()),
                             {'message': 'Hello World'})