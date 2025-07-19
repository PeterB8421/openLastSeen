import os
from os.path import join
import glob
import sys
import re
import platform


def main():
    directory = os.getcwd()
    add = False
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    onlyfiles = []
    for ext in ('mkv', 'avi', 'mp4'):
        pattern = os.path.join(glob.escape(directory), f'*.{ext}')
        onlyfiles.extend(glob.glob(pattern))

    if len(sys.argv) > 2:
        if sys.argv[2] == "a":
            add = True

    if not os.path.isfile(os.path.join(directory, 'seen.txt')):
        with open(os.path.join(directory, 'seen.txt'), 'w') as f:
            pass

    with open(join(directory, "seen.txt"), "r+") as f:
        lines = f.readlines()
        if not lines:
            last_seen = "0"
        else:
            last_seen = lines[len(lines)-1]
        to_play = int(last_seen) + 1
        to_play = str(to_play)
        if add:
            f.write("\n" + to_play)
            exit(0)
        opened = False
        for file in onlyfiles:
            if opened:
                break
            if platform.system() == 'Linux' in file:
                filename = file.rsplit('/')[-1]
            else:
                filename = file.rsplit('\\')[-1]
            if len(to_play) == 1:
                if re.search(r'E0' + to_play, filename):
                    opened = True
                    print(f'Opening file {filename}')
                    os.system("start \"\" \"" + file + "\"")
            else:
                if re.search(r'E' + to_play, filename):
                    opened = True
                    print(f'Opening file {filename}')
                    os.system("start \"\" \"" + file + "\"")

        if not opened:
            print("Could not find episode number " + to_play + " (you may have reached the end of season).")
            input("Press [enter] to continue.")
        return 0


if __name__ == '__main__':
    main()
