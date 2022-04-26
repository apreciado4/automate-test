from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        # self.assertEqual(0, len(b.posts)) Can be used to check for empty list

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('My day', 'Rolf')
        b2.posts = ['test', 'another']
        b3 = Blog('Empty', 'No Author')

        self.assertEqual(b.__repr__(), '<Test by Test Author (1 post)>')
        self.assertEqual(b2.__repr__(), '<My day by Rolf (2 posts)>')
        self.assertEqual(b3.__repr__(), '<Empty by No Author (0 posts)>')

    # Not Unit test, testing two different units!
    def test_create_post(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')
        self.assertEqual(len(b.posts), 1)
