def are_chars_unique(chars):
    if len(set(chars)) == 4:
        return True
    return False


def find_last_unique_char_index(chars):
    unique_chars_dict = {}
    index = 0
    for idx, char in enumerate(chars):
        if char in unique_chars_dict:
            index = unique_chars_dict[char] + 1
        unique_chars_dict[char] = idx

    return index


def find_marker():
    buffer = read_file('input.txt')[0]
    idx = 0
    while True:
        chars = buffer[idx:idx+4]
        if (are_chars_unique(chars)):
            break
        else:
            idx += find_last_unique_char_index(chars)
    print(idx + 4)
    return idx + 4


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    find_marker()
