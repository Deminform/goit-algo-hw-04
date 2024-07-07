import sys
from pathlib import Path
from colorama import Fore, init

# prefix components:
space = '    '
branch = '│   '
# pointers:
tee = '├── '
last = '└── '

init(autoreset=True)


def main(path):
    for line in build_tree(Path(path)):
        print(line)


# Recursive method of building a directory tree
def build_tree(dir_path: Path, prefix=''):
    try:
        contents = list(dir_path.iterdir())
    except FileNotFoundError:
        raise FileNotFoundError('Incorrect path')
    except PermissionError:
        raise PermissionError('Permission denied')

    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        if path.is_dir():
            yield prefix + pointer + Fore.YELLOW + '📂 ' + path.name
            # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from build_tree(path, prefix=prefix + extension)
        else:
            yield prefix + pointer + Fore.MAGENTA + '📜 ' + path.name


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(Path(sys.argv[1]))

