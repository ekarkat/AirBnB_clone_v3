#!/usr/bin/python3
'''Compress a directory ro .tgz'''

from datetime import datetime
from fabric.api import local
from fabric.api import put, env, run, task
import re

env.hosts = ["35.153.93.177", "34.203.77.10"]


def do_pack():
    """Create a tgz archive for web_static."""
    date = datetime.utcnow()
    file_l = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                           date.month,
                                                           date.day,
                                                           date.hour,
                                                           date.minute,
                                                           date.second)

    local("mkdir -p versions")
    try:
        file = file_l.split("/")[-1]
        filename = file.split(".")[0]
        local("tar -cvzf {} web_static".format(file_l))
        pat = "/data/web_static/releases/"
        local("cp {} /tmp/".format(file_l))
        local("mkdir -p {}{}/".format(pat, filename))
        local("tar -xzf /tmp/{} -C {}{}/".format(file, pat, filename))
        local("rm /tmp/{}".format(file))
        local("mv {0}{1}/web_static/* {0}{1}/".format(pat, filename))
        local("rm -rf {}{}/web_static".format(pat, filename))
        local("rm -rf /data/web_static/current")
        local("ln -sf {}{}/ /data/web_static/current".format(pat, filename))
        return (file_l)
    except Exception:
        return (None)


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    try:
        file = archive_path.split("/")[-1]
        filename = file.split(".")[0]
    except Exception:
        return False
    try:
        pat = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(pat, filename))
        run("tar -xzf /tmp/{} -C {}{}/".format(file, pat, filename))
        run("rm /tmp/{}".format(file))
        run("mv {}{}/web_static/* {}{}/".format(pat, filename, pat, filename))
        run("rm -rf {}{}/web_static".format(pat, filename))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}{}/ /data/web_static/current".format(pat, filename))
        return True
    except Exception:
        return False


def deploy():
    """Do_deploy and dp_pack"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
