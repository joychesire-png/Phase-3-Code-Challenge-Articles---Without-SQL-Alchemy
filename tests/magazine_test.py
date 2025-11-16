import pytest
from lib.author import Author
from lib.magazine import Magazine

def test_magazine_creation():
    m = Magazine("Health Weekly", "Health")
    assert m.name == "Health Weekly"
    assert m.category == "Health"

def test_article_titles_and_contributors():
    a = Author("Alice")
    m = Magazine("Tech Today", "Tech")
    a.add_article(m, "Python Basics")
    a.add_article(m, "Advanced Python")
    assert "Python Basics" in m.article_titles()
    assert a in m.contributors()
