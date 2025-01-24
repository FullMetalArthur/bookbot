def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def words_counter(text):
    split_text = text.split()
    words_num = len(split_text)
    return words_num

def char_counter(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def char_dict_sorted(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    text = main()
    word_count = words_counter(text)
    char_count = char_counter(text)
    sorted_list = char_dict_sorted(char_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- end report ---")