from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '
POST_TEMPLATE = '''
        --- {} ---
        
        {}
        '''
blogs = dict()  # blog_name : Blog object


def menu():
    """
    Show the user the available blogs
    Let the user make a choice
    Do Something with that choice
    Eventually exit
    """

    print_blogs()

    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    # Print available blogs
    for key, blog in blogs.items():  # (blog_name, Blog), (blog_name, Blog), (key, value)
        print('- {}'.format(blog))


def ask_create_blog():
    # new_blog_info = input('Please enter blog title and your name! ("Title Name")').strip().split()
    # new_blog = Blog(new_blog_info[0], new_blog_info[1])
    # blogs.update({new_blog.title: new_blog})
    title = input('Please enter the blog title: ')
    author = input('Please enter the blog author: ')
    new_blog = Blog(title, author)
    blogs.update({new_blog.title: new_blog})


def my_ask_read_blog():
    blog_title = input('Please enter the blog title you want to read: ')

    if blog_title not in blogs:
        print('This blog does not exist')
        return
    posts = blogs[blog_title].posts
    print(posts)


def ask_read_blog():
    blog_title = input('Please enter the blog title you want to read: ')

    print_posts(blogs[blog_title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('Please enter blog name: ')
    title = input('Enter post title: ')
    content = input('Enter post content')

    blogs[blog_name].create_post(title, content)


def my_ask_create_post():
    blog_title = input('Please enter blog title!')
    if blog_title not in blogs:
        print("That Blog does not exist")
        return
    new_post_info = input('Please input post title followed by post content ("Test Test Content")').split(' ', 1)
    new_post = blogs[blog_title].create_post(new_post_info[0], new_post_info[1])


if __name__ == '__main__':
    menu()
