#!/usr/bin/env python


import os
import time
import subprocess


config_file_path = os.path.abspath(os.path.dirname(__file__)) + "/fowardlist.txt"


def wrap(commandline):
    print commandline
    time.sleep(0.1)
    return subprocess.Popen(commandline, shell=True)


def getcommand():
    procs = []

    with open(config_file_path, "r") as f:
        for l in f.readlines():
            line = l.strip()

            if not line:
                continue

            comment_pos = line.find(r"#")
            if comment_pos != -1:
                line = line[:comment_pos].strip()

            procs.append([wrap(line), line])

    return procs


def main():
    procs = getcommand()

    try:
        while procs:
            for p, c in procs:
                ret = p.poll()
                if ret is not None:
                    print "finish: ", c
                    print "restarting..."
                    procs.remove(p)
                    procs.append([wrap(c), c])

            else:
                time.sleep(0.1)
                continue

    except KeyboardInterrupt:
        pass

    finally:
        for p, c in procs:
            p.terminate()


if __name__ == "__main__":
    main()
