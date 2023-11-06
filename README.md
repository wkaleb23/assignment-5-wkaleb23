[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XON4KL2y)
# Assignment 5, Fall 2023

### Objectives

* Practice identifying and implementing hierarchical data classes
* Become familiar with pytest testing framework

We are building out a system to calculate the scientific impact of 
various publications. 

You will define a set of classes that captures the data used to calculate the impact. 

## System Specification

The system **estimates the impact** of the following `Publications`: 

* `Article`
* `Book`

An `Article` can be one of: 

* `ConferenceProceeding`
* `Journal`

A `Book` can be one of: 

* `Textbook`
* `EditedVolume`

For every `Publication`, the system keeps track of: 

* `title`, represented as a `String`
* `authors`, represented as a list of `Strings`
* `publishing_year`, represented as an `int`
* `number_of_citations`, represented as an `int`.

Additionally, for every `Book`, the system also keeps track of:

* `publishing_company`, represented as a `String`
* `number_of_pages`, represented as an `Integer`. 

For every `EditedVolume`, the system keeps track of:

* `editors`, represented as a list of `Strings`

For every `Journal`, the system keeps track of:

* `publisher`, represented as a `String`
* `editors`, represented as a list of `Strings`

Finally, for every `Conference proceeding`, the system additionally keeps track of:

* `conference_name`, represented as a `String`.
* `conference_location`, represented as a `String`.

Impact is calculated based on the following rules: 

* **Base impact:** the base impact of every scientific publication is estimated by dividing that publication’s number of citations with an age of that publication.
* **Age of publication:** the age of a publication is found as a difference between the current year (2023) and the publication’s publishing year. If the publishing year is also 2023, the age of the publication is set to 1.
* **Impact of journals:** historically, an impact of books and journals has been considered higher than an impact of conference proceedings. To account for that, a total impact of a journal is computed by multiplying the base impact by factor 2.
  * However, for some reason, conferences held in "Seattle, WA" always have a ton of impact. If the `conference_location` for a `ConferenceProceeding` is `"Seattle, WA"`, the total impact is increased by 25. 
* **Impact of books:** similarly, a total impact of a book is computed by multiplying the base impact by 4.
  * Impact of **Textbooks**: If a book is a Textbook with at least 200 and no more than 500 pages, the impact is increased by 50.
  * Impact of **EditedVolumes**: If an EditedVolume has more than 10 editors (authors), the impact is increased by 25. 
* **Impact of newer publications:** additionally, newer publications are typically considered to be more impactful than older. To account for that, every publication younger than three years gets a "freshness bump", where constant 100 is added to the base impact of that publication.
* **Old publications’ exceptions:** lastly, it has been shown that the presented rules do not provided meaningful estimation of impact for publications older than 250 years. So, if a publication is older than 250 year, the system should not try to estimate the impact according to the given rules. Instead, it should throw an error. 
  * For this assignment, you can throw a `NotImplementedError`. We'll discuss custom errors later. 
  * Example: `raise NotImplementedError`

## Your Task

Design and implement a set of classes representing the publications specified above, 
which method `estimate_impact()`, which returns a `float`. 
That means that, when we call method `estimate_impact()` on some `Publication`, it should return the 
impact of the given scientific publication as a `float`.

All of your classes MUST have an all-args constructor (e.g. a constructor that initializes all fields 
of the object). If you'd like, you can add a *no-args constructor* and *getter/setter* functions. (This would 
enable you to create an empty object and set the various fields individually).

## Running your code

With this assignment, we provide a suite of test cases for you to run using `pytest`.

If you run the following commands and you get an error, you may need to install pytest. Refer 
to the slides from Lecture 8, Slides 20-21 to ensure pytest is installed in your PyCharm 
environment. If it still complains, post to Piazza or ask at OH for guidance. 

Run tests by calling pytest: 
```shell
pytest 
```

I usually prefer to run `pytest -rA` or `pytest -rap` or `pytest -v`

```shell
~/C/F/e/S/assignment-5 ❯❯❯ pytest -rap
======================== test session starts ========================
platform darwin -- Python 3.9.7, pytest-7.4.2, pluggy-1.3.0
rootdir: /Users/adrienne/ClassGits/Fall2023/eep590a/StudentRepos/assignment-5
plugins: anyio-4.0.0
collected 7 items                                                   

a5_test.py .......                                            [100%]

====================== short test summary info ======================
PASSED a5_test.py::TestPublications::test_publication_2authors
PASSED a5_test.py::TestArticle::test_simple_article
PASSED a5_test.py::TestConferenceProceedings::test_simple_confproc
PASSED a5_test.py::TestJournal::test_simple_journal
PASSED a5_test.py::TestBook::test_simple_book
PASSED a5_test.py::TestTextbook::test_simple_textbook
PASSED a5_test.py::TestEditedVolume::test_simple_edited_vol
========================= 7 passed in 0.02s =========================
```
