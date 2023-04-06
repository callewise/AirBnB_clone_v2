#!/usr/bin/python3
from fabric.api import local
from os.path import isdir
from datetime import datetime


def do_pack():
    """ A script that generates .tgz archive the contents of web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
