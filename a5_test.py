import pytest
from pytest import approx
from a5 import *

class TestPublications:

    def test_publication_2authors(self):
        pub = Publication("some title", ["author1", "author2"], 2012, 25)
        ## (25 citations/ 11 yr)
        assert pub.estimate_impact() == approx(2.27272727)

    def test_publication_10yrs(self):
        pub = Publication("some title", ["author1", "author2"], 2013, 100)
        ## (100 citations/ 10 yr)
        assert pub.estimate_impact() == 10

    def test_publication_recent_is_bigger(self):
        pub = Publication("some title", ["author1", "author2"], 2021, 100)
        ## (100 citations/ 2 yr) + 100 [recent]
        assert pub.estimate_impact() == 150

    def test_old_publication_throws_error(self):
        pub = Publication("some title", ["author1", "author2"], 1772, 100)
        with pytest.raises(NotImplementedError):
            pub.estimate_impact()

class TestArticle:
    def test_simple_article(self):
        pub = Article("some title", ["author1", "author2"], 2013, 100)
        assert pub.estimate_impact() == 10

    def test_old_article_throws_error(self):
        pub = Article("some title", ["author1", "author2"], 1772, 100)
        with pytest.raises(NotImplementedError):
            pub.estimate_impact()


class TestConferenceProceedings:
    def test_simple_confproc(self):
        pub = ConferenceProceeding("some title", ["author1", "author2"], 2013, 100, "ConfName1", "ConfLoc1")
        ## (100 citations/ 10 yr)
        assert pub.estimate_impact() == 10

    def test_recent_confproc(self):
        pub = ConferenceProceeding("some title", ["author1", "author2"], 2023, 10, "ConfName1", "ConfLoc1")
        ## (10 citations/ 1 yr) + 100 [recent]
        assert pub.estimate_impact() == 110

    def test_conf_in_seattle(self):
        pub = ConferenceProceeding("some title", ["author1", "author2"], 2013, 100, "ConfName1", "Seattle, WA")
        ## (100 citations/ 10 yr) + 25 [seattle]
        assert pub.estimate_impact() == 35

    def test_recent_conf_in_seattle(self):
        pub = ConferenceProceeding("some title", ["author1", "author2"], 2023, 10, "ConfName1", "Seattle, WA")
        ## (10 citations/ 1 yr) + 100 [recent] + 25 [seattle]
        assert pub.estimate_impact() == 135

    def test_old_conf_proc_throws_error(self):
        pub = ConferenceProceeding("some title", ["author1", "author2"], 1772, 100, "ConfName", "Some Place")
        with pytest.raises(NotImplementedError):
            pub.estimate_impact()

class TestJournal:
    def test_simple_journal(self):
        pub = Journal("some title", ["author1", "author2"], 2013, 100, "Publisher", ["ed1", "ed2"])
        ## (100 citations/ 10 yr) * 2 [journal]
        assert pub.estimate_impact() == 20

    def test_recent_journal(self):
        pub = Journal("some title", ["author1", "author2"], 2023, 10, "Publisher", ["ed1", "ed2"])
        ## (10 citations/ 1 yr) + 100 [recent] * 2 [journal]
        assert pub.estimate_impact() == 220

    def test_old_journal_throws_error(self):
        pub = Journal("some title", ["author1", "author2"], 1772, 100, "Publisher", ["ed1"])
        with pytest.raises(NotImplementedError):
            pub.estimate_impact()

class TestBook:
    def test_simple_book(self):
        pub = Book("some title", ["author1", "author2"], 2013, 100, "PubCompany1", 150)
        ## (100 citations/ 10 yr)  * 4 [book]
        assert pub.estimate_impact() == 40

    def test_recent_book(self):
        pub = Book("some title", ["author1", "author2"], 2023, 10, "PubCompany1", 150)
        ## (10 citations/ 1 yr) + 100 [recent] * 4 [book]
        assert pub.estimate_impact() == 440

    def test_old_book_throws_error(self):
        pub = Book("some title", ["author1", "author2"], 1772, 100, "PubCompany2", 150)
        with pytest.raises(NotImplementedError):
            pub.estimate_impact()


class TestTextbook:
    def test_simple_textbook(self):
        pub = Textbook("some title", ["author1", "author2"], 2012, 25, "PubCompany1", 150)
        ## (25 citations/ 11 yr)  * 4 [book]
        assert pub.estimate_impact() == approx(9.09090909)

    def test_short_old_textbook(self):
        pub = Textbook("some title", ["author1", "author2"], 2013, 100, "PubCompany1", 50)
        ## (10 citations/ 1 yr)  * 4 [book]
        assert pub.estimate_impact() == 40

    def test_long_old_textbook(self):
        pub = Textbook("some title", ["author1", "author2"], 2013, 100, "PubCompany1", 1000)
        ## (100 citations / 10 yrs) * 4 [book]
        assert pub.estimate_impact() == 40

    def test_happylength_old_textbook(self):
        pub = Textbook("some title", ["author1", "author2"], 2013, 100, "PubCompany1", 300)
        ## (100 citations / 10 yrs old) * 4 + 50
        assert pub.estimate_impact() == 90

    def test_happylength_recent_textbook(self):
        pub = Textbook("some title", ["author1", "author2"], 2023, 10, "PubCompany1", 300)
        ## (10 cit / 1 yrs) + 100 [recent] * 4 [book] + 50 [length]
        assert pub.estimate_impact() == 490

    def test_old_textbook_throws_error(self):
        pub = Textbook("some title", ["author1", "author2"], 1772, 100, "Publisher", 150)
        with pytest.raises(NotImplementedError):
            pub.estimate_impact()


# I had to add the editors list
class TestEditedVolume:
    def test_simple_edited_vol(self):
        pub = EditedVolume("some title", ["author1", "author2"], 2013, 100, "PubCompany1", 150, ["ed1", "ed2"])
        ## (100 citations/ 10 yr)  * 4 [book]
        assert pub.estimate_impact() == 40

    def test_recent_edited_vol(self):
        pub = EditedVolume("some title", ["author1", "author2"], 2023, 10, "PubCompany1", 150, ["ed1"])
        ## (10 citations/ 1 yr) + 100 [recent] * 4 [book]
        assert pub.estimate_impact() == 440

    def test_recent_edited_vol_many_authors(self):
        pub = EditedVolume("some title", ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11"], 2023, 10,
                           "PubCompany1", 150,
                           ["ed1", "ed2", "ed3", "ed4", "ed5", "ed6", "ed7", "ed8", "ed9", "ed10", "ed11", "ed12",
                            "ed13"])
        ## (10 citations / 1 yr) + 100 [recent] * 4 [book] + 25 [editors]
        assert pub.estimate_impact() == 465

    def test_old_edited_vol_throws_error(self):
        pub = EditedVolume("some title", ["author1", "author2"], 1772, 100, "Publisher", 50, ["ed1", "ed2"])
        with pytest.raises(NotImplementedError):
            pub.estimate_impact()