def get_book_text(path_to_file):
    with open(path_to_file,) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    print(get_book_text(book_path))

main()