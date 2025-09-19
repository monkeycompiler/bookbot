def get_book_text(path_to_file):
    with open(path_to_file,) as f:
        return f.read()

def get_book_words(input):
    total_words = input.split()
    return len(total_words)