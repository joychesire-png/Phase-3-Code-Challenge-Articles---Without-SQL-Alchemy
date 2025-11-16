class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string 5-50 chars long")
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)
