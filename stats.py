def count_words(book_text):
    num_words = len(book_text.split())
    return num_words


def count_chars(book_text):
    lowered_text = book_text.lower()
    char_count = {}

    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(dict):
    return next(iter(dict.values()))


def pretty_print(char_dict):
    pretty_list = []

    for k, v in char_dict.items():
        if k.isalpha():
            new_small_dict = {k: v}
            pretty_list.append(new_small_dict)
            sort_on(new_small_dict)

    pretty_list.sort(key=sort_on, reverse=True)

    for char_dict in pretty_list:
        char = next(iter(char_dict.keys()))
        count = char_dict[char]
        print(f"{char}: {count}")
