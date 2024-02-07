import os
import argparse

parser = argparse.ArgumentParser(description=
                                 'Give it full path to folder and it\'ll return tree of content with size.')
parser.add_argument('-f',
                    '--folder',
                    help=r'Input a path to folder. Like "/home/user/bin" for Unix and "C:\user\docs\" for Windows',
                    required=True,
                    type=str)
args = parser.parse_args()


def tree_folder(folder):
    if os.path.isdir(folder):
        this_path = tuple(os.walk(folder))
        for i in range(len(this_path)):
            last_slash = this_path[i][0].rfind('/')
            root = this_path[i][0][last_slash + 1:]
            print('├──' * i, end='')
            print(root)
            for j in this_path[i][2]:
                print('├──' * (i + 1), end='')
                print(j, end='')
                try:
                    print(f' - {os.path.getsize(j)} bytes')
                except FileNotFoundError:
                    print(' - Unknown size')
    else:
        print('Something is wrong. Try again')


tree_folder(args.folder)
