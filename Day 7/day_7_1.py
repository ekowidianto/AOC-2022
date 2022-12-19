class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.parent = parent
        self.dirs = {}
        self.files = {}

    def add_size(self, size):
        self.size += size
        if self.parent != None:
            self.parent.add_size(size)

    def add_new_dir(self, name):
        if name not in self.dirs:
            self.dirs[name] = Dir(name, self)

    def add_new_file(self, name, size):
        if name not in self.files:
            self.files[name] = File(name, size, self)
            self.add_size(size)


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent


def parse_ls(cmd):
    cmd_split = cmd.split(" ")
    type_or_size, name = cmd_split[0], cmd_split[1]
    return type_or_size, name


def process_cd(cmd):
    cmd_split = cmd.split(" ")
    return cmd_split[-1]


def setup_dir():
    main_dir = Dir("/", None)
    curr_dir = main_dir
    cmds = read_file('input.txt')
    for cmd in cmds:
        if cmd[:4] == "$ cd":
            cmd_dir = process_cd(cmd)
            if cmd_dir == "/":
                curr_dir = main_dir
            elif cmd_dir == "..":
                curr_dir = curr_dir.parent
            else:
                curr_dir = curr_dir.dirs[cmd_dir]
        elif cmd[:4] == "$ ls":
            continue
        else:
            type_or_size, name = parse_ls(cmd)
            if type_or_size == "dir":
                curr_dir.add_new_dir(name)
            elif name not in curr_dir.files:
                size = int(type_or_size)
                curr_dir.add_new_file(name, size)
    return main_dir


def filter_and_sum_dir(dirs, max_size):
    dir_size_list = list(map(lambda x: x.size, dirs))
    return sum(list(filter(lambda x: x <= max_size, dir_size_list)))


def find_total_dir_size(current_dir):
    child_dirs = list(current_dir.dirs.values())
    if len(child_dirs) == 0:
        return 0
    total = filter_and_sum_dir(child_dirs, 100000)
    for dir_child in child_dirs:
        total += find_total_dir_size(dir_child)

    return total


def read_file(filename):
    with open(filename) as file:
        contents = file.read().splitlines()
    return contents


if __name__ == '__main__':
    current_dir = setup_dir()
    print(find_total_dir_size(current_dir))
