#!/usr/bin/python3
""" Packs Static Content tar """
from fabric.operations import local
from datetime import datetime
from fabric.api import *
import os
from datetime import datetime
import tarfile


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
