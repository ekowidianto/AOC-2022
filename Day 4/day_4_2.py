def is_overlapped(beg_1, end_1, beg_2, end_2):
    if (beg_2 <= end_1 and beg_2 >= beg_1) or (beg_1 <= end_2 and beg_1 >= beg_2):
        return True


def convert_assignment_range_to_int(rng):
    split_rng = rng.split('-')
    return int(split_rng[0]), int(split_rng[1])


def total_overlapped_assignments():
    assignments = read_file('input.txt')
    total_overlapped = 0
    for assignment_pair in assignments:
        assignment_pair_value = assignment_pair.split(',')
        pair1, pair2 = assignment_pair_value[0], assignment_pair_value[1]
        beg_1, end_1 = convert_assignment_range_to_int(pair1)
        beg_2, end_2 = convert_assignment_range_to_int(pair2)
        if is_overlapped(beg_1, end_1, beg_2, end_2):
            total_overlapped += 1
    print(total_overlapped)
    return total_overlapped


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    total_overlapped_assignments()
