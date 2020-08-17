#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the
    contents of the web_static folder
    """
    try:
        time_now = datetime.now().strftime('%Y%m%d%H%M%S')
        arch_name = "web_static_{}".format(str(time_now))
        new_folder = "versions"
        target_path = "{}/{}.tgz".format(new_folder, arch_name)
        source_folder = "web_static"

        initial_msg = "Packing {} to {}".format(source_folder, target_path)
        print(initial_msg)

        with hide('running'):
            local('mkdir -p {}'.format(new_folder))

        local('tar -cvzf {} {}'.format(target_path, source_folder))

        with hide('running'):
            file_size = local(
                'stat -c %s {}'.format(target_path), capture=True)

        final_msg = "{} packed: {} -> {}Bytes".format(
            source_folder, target_path, file_size)
        print(final_msg)

        return target_path

    except Exception:
        return None
