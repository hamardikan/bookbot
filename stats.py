def get_num_words(text):
    return len(text.split())


def get_char_counts(text):
    counts = {}
    for ch in text:
        ch = ch.lower()
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def _sort_on(item):
    return item["num"]


def get_sorted_char_list(char_counts):
    sorted_list = []
    for ch, num in char_counts.items():
        sorted_list.append({"char": ch, "num": num})

    sorted_list.sort(reverse=True, key=_sort_on)
    return sorted_list


# Optional aliases (harmless, can help if tests expect these names)
get_num_chars = get_char_counts
chars_dict_to_sorted_list = get_sorted_char_list
