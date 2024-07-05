from pathlib import Path

# prefix components:
space = '    '
branch = '│   '
# pointers:
tee = '├── '
last = '└── '


def print_tree(path):
    for line in build_tree(Path(path), ''):
        print(line)


def build_tree(dir_path: Path, prefix: str):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from build_tree(path, prefix=prefix + extension)

#
# for line in tree(Path('files_for_test'), ''):
#     print(line)
