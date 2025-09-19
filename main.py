from stats import get_book_text
from stats import get_book_words

def main():
    book_path = "books/frankenstein.txt"
    book_string = get_book_text(book_path)
    num_words = get_book_words(book_string)
    print(f"{num_words} words found in the document")

main()