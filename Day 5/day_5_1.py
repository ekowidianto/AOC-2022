
def initial_position():
    input = {'1': 'DLJRVGF',
             '2': 'TPMBVHJS',
             '3': 'VHMFDGPC',
             '4': 'MDPNGQ',
             '5': 'JLHNF',
             '6': 'NFVQDGTZ',
             '7': 'FDBL',
             '8': 'MJBSVDN',
             '9': 'GLD'}
    for key, value in input.items():
        input[key] = list(value)
    return input


def find_top_of_stacks():
    lines = read_file('input.txt')
    crates = initial_position()
    top_crates = []
    for line in lines:
        line_split = line.split(' ')
        crate_num, src, dst = line_split[1], line_split[3], line_split[5]

        for _ in range(int(crate_num)):
            crate = crates[src].pop()
            crates[dst].append(crate)

    for _, value in crates.items():
        top_crates.append(value[-1])
    print(''.join(top_crates))
    return top_crates


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    find_top_of_stacks()
