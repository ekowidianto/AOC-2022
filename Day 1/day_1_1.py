def max_calories():
    contents = read_file('input.txt')
    maximum = 0
    current = 0
    for content in contents:
        if content == "":
            if maximum < current:
                maximum = current
            current = 0
        else:
            current += int(content)
    return maximum


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    print(max_calories())
