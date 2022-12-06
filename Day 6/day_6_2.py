def are_chars_unique(chars):
    return len(set(chars)) == len(chars)


def find_last_unique_char_index(chars):
    unique_chars_dict = {}
    index = 0
    for idx, char in enumerate(chars):
        if char in unique_chars_dict:
            index = unique_chars_dict[char] + 1
        unique_chars_dict[char] = idx

    return index


def find_marker(distinct_chars):
    buffer = read_file('input.txt')[0]
    idx = 0
    while True:
        chars = buffer[idx:idx+distinct_chars]
        if (are_chars_unique(chars)):
            break
        else:
            idx += find_last_unique_char_index(chars)
    print(idx + distinct_chars)
    return idx + distinct_chars


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    find_marker(14)
