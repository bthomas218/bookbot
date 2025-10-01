def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
main()