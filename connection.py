#!/usr/bin/python3
'''Compress a directory ro .tgz'''

from datetime import datetime
from fabric import Connection
from invoke import run as local
from fabric import task

con1 = Connection("alx1")
con2 = Connection("alx2")

connections = [con1, con2]

file = "web_static_20231210235730"

for con in connections:
    print("server : {}".format(con.host))
    # transfer the file to tmp
    print("transfer the file to tmp")
    con.put("versions/{}.tgz".format(file), "/tmp/")
    con.run("mkdir -p /data/web_static/releases/{}/".format(file))
    # extract the arvhive in data/web_static/releases
    print("extract the arvhive in data/web_static/releases")
    con.run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}".format(file, file))
    # remove the archive in tmp
    print("remove the archive in tmp")
    con.run("rm -f /tmp/{}.tgz".format(file))
    # rm /data/web_static/current
    print("rm /data/web_static/current")
    con.run("rm -rf /data/web_static/current")
    # move files in /web_static to <archive filename>
    con.run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(file, file))
    # remove webstatic folder
    con.run("rm -rf /data/web_static/releases/{}/web_static/".format(file))
    # create a symbolic link
    print("create a symbolic link")
    con.run("ln -sf /data/web_static/releases/{} /data/web_static/current".format(file))
