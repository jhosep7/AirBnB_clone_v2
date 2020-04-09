#!/usr/bin/python3
""" Deploy AirBnB2"""

from fabric.api import *
import os

env.hosts = ["35.227.16.88", "54.144.228.69"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploys to servers"""
    if not os.path.exists(archive_path):
        return False
    MyArr = []
    MyFacts = put(archive_path, "/tmp")
    MyArr.append(MyFacts.succeeded)
    filename = os.path.filename(archive_path)
    if filename[-4:] == ".tgz":
        name = filename[:-4]
    DirNew = "/data/web_static/releases/" + name
    run("mkdir -p " + DirNew)
    run("tar -xzf /tmp/" + filename + " -C " + DirNew)
    run("rm /tmp/" + filename)
    run("mv " + DirNew + "/web_static/* " + DirNew)
    run("rm -rf " + DirNew + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + DirNew + " /data/web_static/current")
    return True
