import sys
from stats import count_words, count_characters, list_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])

    num_words = count_words(text)
    char_counter = count_characters(text)

    print(f"Found {num_words} total words")
    for item in list_characters(char_counter):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
main()