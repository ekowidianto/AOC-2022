def find_rucksack_priority(rucksack):
    rucksack_len = len(rucksack)
    first_compartment = rucksack[:int(rucksack_len / 2)]
    second_compartment = rucksack[int(rucksack_len / 2):]
    first_compartment_set = set()
    for item in first_compartment:
        first_compartment_set.add(item)
    for item in second_compartment:
        if item in first_compartment_set:
            return item


def calculate_rucksack_priority_num(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1


def sum_rucksacks_priorities():
    rucksacks = read_file('input.txt')
    total_points = 0
    for rucksack in rucksacks:
        rucksack_priority = find_rucksack_priority(rucksack)
        total_points += calculate_rucksack_priority_num(rucksack_priority)
    print(total_points)
    return total_points


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    sum_rucksacks_priorities()
