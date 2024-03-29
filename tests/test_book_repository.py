from lib.book_repository import BookRepository
from lib.book import Book

# Test that when we call the BookRepository all function
# we get a list of Book objects reflecting seed data
def test_all(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)

    books = repository.all()

    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]