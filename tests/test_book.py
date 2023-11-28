from lib.book import Book

# Test that Book class contructs with an id, title and author_name
def test_book_contruct():
    book = Book(1, "test title", "test author")
    assert book.id == 1
    assert book.title == "test title"
    assert book.author_name == "test author"

# When I contruct two books with the same fields they are equal
def test_equality():
    book1 = Book(1, "test title1", "test author1")
    book2 = Book(2, "test title2", "test author2")

# Test that string format is the same as the requirement
def test_string_format():
    book = Book(1, "test title", "test author")
    assert str(book) == "1 - test title - test author"