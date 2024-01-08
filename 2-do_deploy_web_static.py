#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import *
import re

env.hosts = ["35.153.93.177", "34.203.77.10"]


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
