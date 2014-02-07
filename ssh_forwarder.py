#!/usr/bin/env python


import time
import subprocess


def wrap(commandline):
    print commandline
    time.sleep(0.1)
    return subprocess.Popen(commandline, shell=True)


procs = [
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21100:192.168.4.49:3306 repo"),   # evdb mysql
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21101:192.168.4.246:3306 repo"),  # evdb_second mysql

    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21200:192.168.4.89:22 repo"),     # hadclient ssh
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21201:192.168.4.80:50030 repo"),  # namenode hadoop jobtracker
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21202:192.168.4.80:50070 repo"),  # namenode hadoop hdfs
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21203:192.168.4.80:60010 repo"),  # namenode hadoop hbase

    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21300:192.168.0.49:22 repo"),     # ym0vm ssh
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21301:192.168.0.49:5000 repo"),   # ym0vm cloudforecast
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21302:192.168.0.49:80 repo"),     # ym0vm http

    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21400:192.168.0.211:8000 repo"),  # githost redmine
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21401:192.168.0.211:8001 repo"),  # githost gitlab
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21402:192.168.0.211:80 repo"),    # githost http

    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21500:192.168.0.211:443 repo"),   # githost https
    wrap(r"ssh -o ServerAliveInterval=15 -NCL 21501:192.168.0.211:22 repo"),    # githost ssh
]


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    for p in procs:
        p.terminate()

