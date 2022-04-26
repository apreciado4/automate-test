from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        plural = 's' if len(self.posts) != 1 else ''
        return f'<{self.title} by {self.author} ({len(self.posts)}post{plural})>'

    def create_post(self, title, content):
        p = Post(title, content)
        self.posts.append(p)

    def json(self):
        dict_blog = {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }
        return dict_blog
