import sys
from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage:  python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' does not exist")
        sys.exit(1)

    return text, book_path

if __name__ == "__main__":
    text, book_path = main()
    word_count = words_counter(text)
    char_count = char_counter(text)
    sorted_list = char_dict_sorted(char_count)
    print("================= BOOKBOT ==================")
    print(f"Analizing book found at {book_path} ...")
    print("---------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("=================== END ====================")