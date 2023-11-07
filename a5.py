"""
Define a class (Publication) that keeps track of:
    title, represented as a String
    authors, represented as a list of Strings
    publishing_year, represented as an int
    number_of_citations, represented as an int.
"""


class Publication:
    def __init__(self, title, authors, publishing_year, number_of_citations):
        self.title = title
        self.authors = authors
        self.publishing_year = publishing_year
        self.number_of_citations = number_of_citations

    # the base impact of every scientific publication is estimated by dividing that publication’s number of citations
    # with an age of that publication.
    def calculate_base_impact(self, age):
        base = self.number_of_citations / age
        return float(base)

    # the age of a publication is found as a difference between the current year (2023) and the publication’s
    # publishing year. If the publishing year is also 2023, the age of the publication is set to 1. lastly,
    # it has been shown that the presented rules do not provided meaningful estimation of impact for publications
    # older than 250 years. So, if a publication is older than 250 year, the system should not try to estimate the
    # impact according to the given rules. Instead, it should throw an error.
    def calculate_age(self):
        current_year = 2023
        if self.publishing_year == current_year:
            return 1
        elif self.publishing_year > current_year:
            raise NotImplementedError
        # if the publication is older than 250 years then raise a NotImplementedError
        elif current_year - self.publishing_year > 250:
            raise NotImplementedError
        return current_year - self.publishing_year

    # additionally, newer publications are typically considered to be more impactful than older. To account for that,
    # every publication younger than three years gets a "freshness bump", where constant 100 is added to the base
    # impact of that publication.
    def freshness_bump(self, age):
        if age < 3:
            return 100
        return 0

    # the base is the same for all publications, so we can define it in the parent class
    def estimate_impact(self):
        age = self.calculate_age()
        base = self.calculate_base_impact(age)
        freshness = self.freshness_bump(age)
        return float(base + freshness)


'''
Article inherits from Publication
'''


class Article(Publication):
    # inherits the constructor from Publication, nothing to add
    def __init__(self, title, authors, publishing_year, number_of_citations):
        super().__init__(title, authors, publishing_year, number_of_citations)

    # same as Publication, so we can use the parent class's method
    # already has the freshness bump added, so we can just return the base
    def estimate_impact(self):
        impact = super().estimate_impact()
        return float(impact)


'''
ConferenceProceeding inherits from Article. It also keeps track of:
    conference_name, represented as a String
    conference_location, represented as a String
'''


class ConferenceProceeding(Article):
    # adds conference_name and conference_location to the constructor
    def __init__(self, title, authors, publishing_year, number_of_citations, conference_name, conference_location):
        super().__init__(title, authors, publishing_year, number_of_citations)
        self.conference_name = conference_name
        self.conference_location = conference_location

    # However, for some reason, conferences held in "Seattle, WA" always have a ton of impact. If the
    # `conference_location` for a `ConferenceProceeding` is `"Seattle, WA"`, the total impact is increased by 25.
    # has already had the freshness bump added
    def estimate_impact(self):
        # calls the Article's estimate_impact() method
        article_base = super().estimate_impact()
        if self.conference_location == "Seattle, WA":
            article_base += 25
        return float(article_base)


'''
Journal inherits from Article. It also keeps track of:
    publisher, represented as a String
    editors, represented as a list of Strings
'''


class Journal(Article):
    # adds publisher and editors to the constructor
    def __init__(self, title, authors, publishing_year, number_of_citations, publisher, editors):
        super().__init__(title, authors, publishing_year, number_of_citations)
        self.publisher = publisher
        self.editors = editors

    # historically, an impact of books and journals has been considered higher than an impact of conference
    # proceedings. To account for that, a total impact of a journal is computed by multiplying the base impact by
    # factor 2.
    # has already had the freshness bump added
    def estimate_impact(self):
        # calls the Article's estimate_impact() method
        article_base = super().estimate_impact()
        return float(article_base * 2)


'''
Book inherits from Publication. It also keeps track of:
    publishing_company, represented as a String
    number_of_pages, represented as an int
'''


class Book(Publication):
    # adds publishing_company and number_of_pages to the constructor
    def __init__(self, title, authors, publishing_year, number_of_citations, publishing_company, number_of_pages):
        super().__init__(title, authors, publishing_year, number_of_citations)
        self.publishing_company = publishing_company
        self.number_of_pages = number_of_pages

    # similarly, a total impact of a book is computed by multiplying the base impact by 4..
    # has already had the freshness bump added
    def estimate_impact(self):
        # calls the Publication's estimate_impact() method
        base = super().estimate_impact() * 4
        return float(base)


'''
Textbook inherits from Book.
'''


class Textbook(Book):
    # nothing to add to the constructor
    def __init__(self, title, authors, publishing_year, number_of_citations, publishing_company, number_of_pages):
        super().__init__(title, authors, publishing_year, number_of_citations, publishing_company, number_of_pages)

    # If a book is a Textbook with at least 200 and no more than 500 pages, the impact is increased by 50.
    # has already had the freshness bump added
    # has already been multiplied by 4, so we can just add 50
    def estimate_impact(self):
        # uses the Book's estimate_impact() method
        book_base = super().estimate_impact()
        # if a textbook has at least 200 pages and no more than 500 pages, then the total impact is increased by 50.
        if 200 <= self.number_of_pages <= 500:
            book_base += 50
        return float(book_base)


'''
EditedVolume inherits from Book. It also keeps track of:
    editors, represented as a list of Strings
'''


class EditedVolume(Book):
    # adds editors to the constructor
    def __init__(self, title, authors, publishing_year, number_of_citations, publishing_company, number_of_pages,
                 editors):
        super().__init__(title, authors, publishing_year, number_of_citations, publishing_company, number_of_pages)
        self.editors = editors

    # If an EditedVolume has more than 10 editors (authors), the impact is increased by 25.
    # has already had the freshness bump added
    # has already been multiplied by 4, so we can just add 25
    def estimate_impact(self):
        # uses the Book's estimate_impact() method
        book_base = super().estimate_impact()
        # if an edited volume has at least 10 editors, then the total impact is increased by 25.
        if len(self.editors) >= 10:
            book_base += 25
        return float(book_base)
