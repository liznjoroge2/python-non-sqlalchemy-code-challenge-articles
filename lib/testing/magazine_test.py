import pytest
from classes.many_to_many import Article, Magazine, Author

class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_has_name(self):
        """magazine is initialized with a name"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_immutable_string(self):
        """magazine name is of type str and cannot change"""
        magazine = Magazine("Vogue", "Fashion")

        assert isinstance(magazine.name, str)

        with pytest.raises(ValueError):
            magazine.name = 123

    def test_name_len(self):
        """magazine name is of correct length"""
        with pytest.raises(ValueError):
            Magazine("", "Fashion")
        with pytest.raises(ValueError):
            Magazine("A"*17, "Fashion")

    def test_has_category(self):
        """magazine is initialized with a category"""
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.category == "Fashion"

    def test_category_is_mutable_string(self):
        """magazine category is of type str and can change"""
        magazine = Magazine("Vogue", "Fashion")
        magazine.category = "Lifestyle"
        assert magazine.category == "Lifestyle"

    def test_has_many_articles(self):
        """magazine has many articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert len(magazine.articles()) == 2
        assert article_1 in magazine.articles()
        assert article_2 in magazine.articles()

    def test_articles_of_type_articles(self):
        """magazine articles are of type Article"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert isinstance(magazine.articles()[0], Article)
        assert isinstance(magazine.articles()[1], Article)
