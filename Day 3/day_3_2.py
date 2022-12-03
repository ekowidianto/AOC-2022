def find_common_badge(group_rucksacks):
    return set(group_rucksacks[0]) & set(group_rucksacks[1]) & set(group_rucksacks[2])


def calculate_rucksack_priority_num(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1


def sum_rucksacks_priorities():
    rucksacks = read_file('input.txt')
    total_points = 0
    group_rucksacks = []
    for index, rucksack in enumerate(rucksacks):
        group_rucksacks.append(rucksack)
        if index != 0 and (index + 1) % 3 == 0:
            common_badge = find_common_badge(group_rucksacks)
            group_rucksacks = []
            total_points += calculate_rucksack_priority_num(common_badge.pop())
            continue
    print(total_points)
    return total_points


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    sum_rucksacks_priorities()
