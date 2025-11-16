class Author:
    def __init__(self, name):
        # Validate name and store
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        self._articles = []
            

    @property
    def name (self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        # Return unique list of magazines this author has written for
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        from lib.article import Article
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        magazine.articles().append(new_article)
        return new_article

    def topic_areas(self):
        mags = self.magazines()
        return list({mag.category for mag in mags}) if mags else None