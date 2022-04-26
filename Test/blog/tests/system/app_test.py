from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    @patch('builtins.input', side_effect =('c', 'Test', 'Test Author', 'q'))
    def test_menu_calls_create_blog(self, mock_input):
        app.menu()

        self.assertIsNotNone(app.blogs['Test'])
        # Can be used with patch('app.ask_create_blog)
        # mock_ask_create_blog.assert_called()

    @patch('builtins.input', return_value='q')
    def test_menu_prints_prompt(self, mocked_input):
        app.menu()
        mocked_input.assert_called_with('Enter "c" to create a blog, "l" to list blogs, "r" to read one, '
                                        '"p" to create a post, or "q" to quit: ')

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mock_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mock_print_blogs.assert_called()

    @patch('app.print_blogs')
    @patch('builtins.input', return_value='q')  # Does not need return value but can be used to test
    def test_menu_calls_print_blogs_with_decorators(self, mock_input, mock_print_blogs):
        app.menu()
        mock_print_blogs.assert_called()

    @patch('app.print_posts')
    @patch('builtins.input', side_effect=('r', 'Test', 'q'))
    def test_menu_calls_ask_read_blog(self, mock_input, mock_print_posts):
        # blog = Blog('Test', 'Test Author')
        # app.blogs = {'Test': blog}
        blog = app.blogs['Test']
        app.menu()

        mock_print_posts.assert_called_with(blog)

    @patch('app.Blog.create_post')
    @patch('builtins.input', side_effect=('p', 'Test', 'Test Title', 'Test Content', 'q'))
    def test_menu_calls_ask_create_post(self, mock_input, mock_ask_create_post):
        # blog = Blog('Test', 'Test Author')
        # app.blogs = {'Test': blog}
        app.menu()

        mock_ask_create_post.assert_called_with('Test Title', 'Test Content')

    def test_print_blogs(self):
        # blog = Blog('Test', 'Test Author')
        # app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- <Test by Test Author (0 posts)>')

    @patch('builtins.print')
    def test_print_blogs_with_decorator(self, mocked_print):
        # blog = Blog('Test', 'Test Author')
        # app.blogs = {'Test': blog}

        app.print_blogs()
        mocked_print.assert_called_with('- <Test by Test Author (0 posts)>')

    @patch('builtins.input', side_effect=('Test', 'Test Author'))
    def test_ask_create_blog(self, mock_input):
        app.ask_create_blog()

        self.assertIsNotNone(app.blogs.get('Test'))

    @patch('builtins.input', return_value='Test')
    @patch('app.print_posts')
    def test_ask_read_blog(self, mock_print_posts, mock_input):
        # blog = Blog('Test', 'Test Author')
        # app.blogs = {'Test': blog}
        blog = app.blogs['Test']
        app.ask_read_blog()

        mock_print_posts.assert_called_with(blog)

    @patch('app.print_post')
    def test_print_posts(self, mock_print_post):
        # blog = Blog('Test', 'Test Author')
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        app.print_posts(blog)

        mock_print_post.assert_called_with(blog.posts[0])

    @patch('builtins.print')
    def test_print_post(self, mock_print):
        post = Post('Post title', 'Post content')
        app.print_post(post)
        expected = '''
        --- Post title ---
        
        Post content
        '''
        mock_print.assert_called_with(expected)

    @patch('builtins.input', side_effect = ('Test', 'Test Title', 'Test Content'))
    def test_ask_create_post(self, mock_input):
        # blog = Blog('Test', 'Test Author')
        # app.blogs = {'Test': blog}
        blog = app.blogs['Test']
        app.ask_create_post()

        self.assertEqual(blog.posts[0].title, 'Test Title')
        self.assertEqual(blog.posts[0].content, 'Test Content')