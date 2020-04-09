#!/usr/bin/python3
""" Cleans Up the whole deployment"""
from datetime import datetime
from fabric.api import *
import tarfile
import os

env.hosts = ["35.227.16.88", "54.144.228.69"]
env.user = "ubuntu"


def do_clean(number=0):
    """ Deletes """
    number = int(number)
    if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
