import os
import argparse


"""Creating parser and description, help for it."""

parser = argparse.ArgumentParser(description=
                                 '''Give it full path to folder and it\'ll return tree of content with size.
                                 Try ''')
parser.add_argument('-f',
                    '--folder',
                    help=r'Input a path to folder. Like "/home/user/bin" for Unix and "C:\user\docs\" for Windows',
                    required=True,
                    type=str)
args = parser.parse_args()


def tree_folder(folder):
    """Shows inside of folder as tree with size of files.
    Takes path of folder that user gives,
    checks is it full path (if it's not - asks for another try)
    than finds last slash in every path that is shown by os.walk.
    That helps to find roots, folders.
    Then indexes os.walk to find names of files.
    And after that generates text as tree of insides of folder.
    Size of files is included.
    """
    if os.path.isdir(folder):
        this_path = tuple(os.walk(folder))
        index_of_path = 0
        index_of_file = 2
        for index_os_walk in range(len(this_path)):
            last_slash = this_path[index_os_walk][index_of_path].rfind('/')
            root = this_path[index_os_walk][index_of_path][last_slash + 1:]
            print('├──' * index_os_walk, end='')
            print(root)
            for j in this_path[index_os_walk][index_of_file]:
                print('├──' * (index_os_walk + 1), end='')
                print(j, end='')
                try:
                    print(f' - {os.path.getsize(j)} bytes')
                except FileNotFoundError:
                    print(' - Unknown size')
    else:
        print('Something is wrong. Try again')


if __name__ == '__main__':
    tree_folder(args.folder)
