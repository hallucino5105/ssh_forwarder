#!/usr/bin/env python


import os
import time
import subprocess


config_file_path = ""
if not os.path.islink(__file__):
    config_file_path = os.path.abspath(os.path.dirname(__file__)) + "/forwardlist.txt"
else:
    config_file_path = os.path.dirname(os.path.realpath(__file__)) + "/forwardlist.txt"


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

            if line:
                procs.append([wrap(line), line])

    return procs


def main():
    procs = getcommand()

    try:
        while procs:
            for l in procs:
                proc, cmd = l

                ret = proc.poll()
                if ret is not None:
                    print "finish: \"%s\"" % cmd
                    print "restarting..."
                    procs.remove(l)
                    procs.append([wrap(cmd), cmd])

            else:
                time.sleep(0.1)
                continue

    except KeyboardInterrupt:
        pass

    finally:
        for proc, cmd in procs:
            proc.terminate()


if __name__ == "__main__":
    main()
