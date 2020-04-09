#!/usr/bin/python3
""" Packs Static Content tar """
from fabric.operations import local
from datetime import datetime
from fabric.api import *
import os
from datetime import datetime
import tarfile


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

if __name__ == "__main__":
    do_pack()
