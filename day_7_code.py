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
    def __init__(self, name, parent=None, size=None) -> None:
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


def large_file_sum(max_size, sample=None):
    home = Directory('/')
    current = home
    listing = False
    with open('day_7_input.txt') as f:
        if sample is None:
            text = f.read().splitlines()
        else:
            text = sample
        for unsplit_line in text:
            line = unsplit_line.split()
            if listing:
                if line[0] == 'dir':
                    line[1] = new_dir = Directory(line[1])
                    current.children.append(new_dir)
                else:
                    line[1] = new_file = File(line[1], line[0])
                    new_file.add_to_size(line[0])
                    current.children.append(new_file)
            if line[1] == 'cd':
                if line[2] == '/':
                    current = home
                elif line[2] == '..':
                    current = current.parent
            elif line[1] == 'ls':
                listing = True


print(large_file_sum(100000))
