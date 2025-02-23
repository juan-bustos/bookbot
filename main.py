import sys
from stats import count_words, count_chars, pretty_print


def get_book_contents(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_contents(sys.argv[1])
    word_count = count_words(book_text)
    chars_dict = count_chars(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    pretty_print(chars_dict)
    print("============= END ===============")


if __name__ == "__main__":
    main()
