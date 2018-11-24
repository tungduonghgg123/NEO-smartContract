class proposal:
    def __init__(self, addr, title, content, token):
        self.title = title
        self.content = content
        self.expTime = token * 60
        self.