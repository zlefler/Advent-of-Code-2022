from collections import deque

'''cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.

To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. 
(This process can count files more than once!)'''


class Directory():
    def __init__(self, name, parent=None, size=0) -> None:
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size

    def add_to_size(self, size):
        self.size += size
        if self.parent:
            self.parent.add_to_size(size)


class File():
    def __init__(self, name, size) -> None:
        self.size = size
        self.name = name


def build_directory(sample=None):
    home = Directory('/')
    current = home
    listing = False
    with open('day_7_input.txt') as f:
        if sample is None:
            text = f.read().splitlines()
        for unsplit_line in text:
            line = unsplit_line.split()
            if listing:
                if line[0] == 'dir':
                    new_dir = Directory(line[1], current)
                    current.children.append(new_dir)
                elif line[0].isnumeric():
                    new_file = File(line[1], int(line[0]))
                    current.add_to_size(int(line[0]))
                    current.children.append(new_file)
                else:
                    listing = False
            if line[1] == 'cd':
                if line[2] == '/':
                    current = home
                elif line[2] == '..':
                    current = current.parent
                else:
                    for child in current.children:
                        if child.name == line[2]:
                            current = child
            elif line[1] == 'ls':
                listing = True
    return home


def sum_of_small_dirs(directory, max_size):
    total = 0
    dir = None
    directory
    dirs = deque()
    dirs.append(directory)
    while dirs:
        for _ in range(len(dirs)):
            dir = dirs.popleft()
            if isinstance(dir, Directory):
                for child in dir.children:
                    dirs.append(child)
            if dir.size <= max_size:
                total += dir.size
    return total


home = build_directory()

print(sum_of_small_dirs(home, 100000))
