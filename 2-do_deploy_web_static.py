#!/usr/bin/python3
""" Deploy AirBnB2"""
from fabric.operations import local, run, put, env
from datetime import datetime
from fabric.api import *
import os

env.hosts = ["35.227.16.88", "54.144.228.69"]
env.user = "ubuntu"


def do_pack():
    """ Builds tar """
    name = "versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None


def do_deploy(archive_path):
    """ Full Deploy to servers"""
    if not os.path.exists(archive_path):
        return False
    Complete = []
    Ans = put(archive_path, "/tmp")
    Complete.append(Ans.succeeded)
    basename = os.path.basename(archive_path)
    if basename[-4:] == ".tgz":
        name = basename[:-4]
    newdir = "/data/web_static/releases/" + name
    run("mkdir -p " + newdir)
    run("tar -xzf /tmp/" + basename + " -C " + newdir)

    run("rm /tmp/" + basename)
    run("mv " + newdir + "/web_static/* " + newdir)
    run("rm -rf " + newdir + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + newdir + " /data/web_static/current")
    return True
