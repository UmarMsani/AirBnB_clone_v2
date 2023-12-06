#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder"""
    now = datetime.utcnow()
    archive_name = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    folder_path = "versions"

    # Create versions folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the tgz archive
    tgz_path = folder_path + "/" + archive_name
    command = "tar -cvzf {} web_static".format(tgz_path)
    result = local(command)

    if result.failed:
        return None
    else:
        return tgz_path
