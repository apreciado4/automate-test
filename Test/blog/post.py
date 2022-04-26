class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f'<Title is {self.title}, Content is {self.content}>'

    def json(self):
        dict_post = {
            'title': self.title,
            'content': self.content,
        }
        return dict_post
