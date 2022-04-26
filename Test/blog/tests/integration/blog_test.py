from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    # Not Unit test, testing two different units!
    def test_create_post(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')
        self.assertEqual(len(b.posts), 1)

    def test_empty_json(self):
        b = Blog('Test', 'Test Author')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': []
        }

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [{
                'title': 'Test Post',
                'content': 'Test Content'
            }]
        }

        self.assertDictEqual(expected, b.json())
