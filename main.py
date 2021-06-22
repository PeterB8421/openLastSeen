import os
from os import listdir
from os.path import isfile, join
from pymediainfo import MediaInfo
import sys


def main():
    dir = os.getcwd()
    add = False
    if len(sys.argv) > 1:
        dir = sys.argv[1]
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    if len(sys.argv) > 2:
        if sys.argv[2] == "a":
            add = True

    if not "seen.txt" in onlyfiles:
        print("seen.txt not found!")
        exit(1)
    with open(join(dir, "seen.txt"), "r+") as f:
        lines = f.readlines()
        if not lines:
            last_seen = "0"
        else:
            last_seen = lines[len(lines)-1]
        to_play = int(last_seen) + 1
        to_play = str(to_play)
        if add:
            # lines.append(to_play)
            f.write("\n" + to_play)
            exit(0)
        opened = False
        for file in onlyfiles:
            file_info = MediaInfo.parse(join(dir, file))
            for track in file_info.tracks:
                if track.track_type == "Video":
                    if "E" + to_play.zfill(2) in file:
                        print("Opening file:")
                        print(file)
                        opened = True
                        os.system("start \"\" \"" + join(dir, file) + "\"")
                    break
        if not opened:
            print("Could not find episode number " + to_play + "(you may have reached the end of season).")
            input("Press [enter] to continue.")
        return 0


if __name__ == '__main__':
    main()
