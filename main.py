from stats import count_words, count_characters, list_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    char_counter = count_characters(text)
    print(f"Found {num_words} total words")
    for item in list_characters(char_counter):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
main()