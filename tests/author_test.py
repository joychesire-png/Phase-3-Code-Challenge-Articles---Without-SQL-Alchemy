import pytest
from lib.author import Author
from lib.magazine import Magazine

def test_author_name():
    a = Author("Alice")
    assert a.name == "Alice"

def test_author_invalid_name():
    with pytest.raises(ValueError):
        Author("")  # Empty string should raise ValueError

def test_add_article_and_magazines():
    a = Author("Bob")
    m = Magazine("Tech Today", "Technology")
    article = a.add_article(m, "Python 101")
    assert article.title == "Python 101"
    assert a.articles()[0] == article
    assert a.magazines()[0] == m
