#!/usr/bin/env python


import os
import time
import subprocess


config_file_path = "./fowardlist.txt"


def wrap(commandline):
    print commandline
    time.sleep(0.1)
    return subprocess.Popen(commandline, shell=True)


def getcommand():
    procs = []
    filepath = "%s/%s" % (os.path.abspath(os.path.dirname(__file__)), config_file_path)

    with open(filepath, "r") as f:
        for l in f.readlines():
            line = l.strip()

            if not line:
                continue

            comment_pos = line.find(r"#")
            if comment_pos != -1:
                line = line[:comment_pos].strip()

            procs.append(wrap(line))

    return procs


def main():
    procs = getcommand()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        for p in procs:
            p.terminate()


if __name__ == "__main__":
    main()
