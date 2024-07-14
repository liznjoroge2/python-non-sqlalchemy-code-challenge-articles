import pytest
from classes.many_to_many import Article, Magazine, Author

class TestArticle:
    """Article in many_to_many.py"""

    def test_has_title(self):
        """Article is initialized with a title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        
        assert article.title == "How to wear a tutu with style"

    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert isinstance(article_1.title, str)

        with pytest.raises(Exception):
            Article(author, magazine, 500)

        with pytest.raises(AttributeError):
            article_1.title = "New Title"

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert 5 <= len(article_1.title) <= 50

        with pytest.raises(ValueError):
            Article(author, magazine, "Test")

        with pytest.raises(ValueError):
            Article(author, magazine, "A" * 51)

    def test_get_all_articles(self):
        """Article class has all attribute"""
        Article.all = []
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert len(Article.all) == 2
        assert article_1 in Article.all
        assert article_2 in Article.all

    def test_has_author(self):
        """article has an author"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        
        assert article.author == author

    def test_author_is_mutable(self):
        """author is of type Author and mutable"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author_1, magazine, "How to wear a tutu with style")
        
        assert article.author == author_1
        
        article.author = author_2
        assert article.author == author_2
        
        with pytest.raises(ValueError):
            article.author = "Not an Author"

    def test_has_magazine(self):
        """article has a magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = Article(author, magazine, "How to wear a tutu with style")
        
        assert article.magazine == magazine

    def test_magazine_is_mutable(self):
        """magazine is of type Magazine and mutable"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article = Article(author, magazine_1, "How to wear a tutu with style")
        
        assert article.magazine == magazine_1
        
        article.magazine = magazine_2
        assert article.magazine == magazine_2
        
        with pytest.raises(ValueError):
            article.magazine = "Not a Magazine"
