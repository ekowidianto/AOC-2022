from queue import PriorityQueue


def max_k_calories(k):
    priority_queue = PriorityQueue()
    current = 0
    contents = read_file('input.txt')
    for content in contents:
        if content == "":
            priority_queue.put((-current, current))
            current = 0
        else:
            current += int(content)
    total_calories = 0
    for _ in range(k):
        total_calories += priority_queue.get()[1]
    return total_calories


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    print(max_k_calories(3))
