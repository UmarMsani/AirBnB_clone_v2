#!/usr/bin/python3
from fabric.api import *
import os

env.hosts = ['54.144.198.163', '52.91.202.177']


def do_clean(number=0):
    """delete old out-of-date archives

    Args:
        number (int): is the number of archives to keep

    If num is zero or 1, keep only the most recent archive. if
    num is two, keeps the most and second-most recent archive,
    etc
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
