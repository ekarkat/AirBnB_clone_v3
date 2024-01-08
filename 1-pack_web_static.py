#!/usr/bin/python3
'''Compress a directory ro .tgz'''

from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tgz archive for web_static."""
    date = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}".format(date.year,
                                                     date.month,
                                                     date.day,
                                                     date.hour,
                                                     date.minute,
                                                     date.second)

    local("mkdir -p versions")
    try:
        local("tar -cvzf {}.tgz web_static".format(file))
        return ("{}.tgz".format(file))
    except Exception:
        return (None)
