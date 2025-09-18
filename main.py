def get_book_text(path_to_file):
    with open(path_to_file,) as f:
        return f.read()

def get_book_words(input):
    total_words = input.split()
    return len(total_words)

def main():
    book_path = "books/frankenstein.txt"
    book_string = get_book_text(book_path)
    num_words = get_book_words(book_string)
    print(f"{num_words} words found in the document")

main()