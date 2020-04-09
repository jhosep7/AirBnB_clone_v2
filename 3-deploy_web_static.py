#!/usr/bin/python3
""" Full Deployment """
from fabric.api import *
import os
from datetime import datetime
import tarfile

env.hosts = ["35.227.16.88", "54.144.228.69"]
env.user = "ubuntu"


def do_pack():
    """ compress web-static into a .tgz """
    DirSave = "versions/"
    NameF = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(DirSave):
        os.mkdir(DirSave)
    with tarfile.open(DirSave + NameF, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(DirSave + NameF):
        return DirSave + NameF
    else:
        return None

def do_deploy(archive_path):
    """ It Deploys to  both servers"""
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

def deploy():
    """ Calls stuff to deploy"""
    tar = do_pack()
    if tar is False:
        return False
    return do_deploy(tar)

if __name__ == "__main__":
    deploy()
