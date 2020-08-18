#!/usr/bin/python3
from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['34.74.122.27', '35.243.238.143']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not path.isfile(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    remote_path = "/tmp/{}".format(file_name)

    put(archive_path, remote_path)
    run('mkdir -p /data/web_static/releases/{}/'
        .format(file_name.split('.')[0]))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(file_name, file_name.split('.')[0]))
    run('rm /tmp/{}'.format(file_name))
    run('mv /data/web_static/releases/{0}/web_static/* \
    /data/web_static/releases/{0}/'.format(file_name.split('.')[0]))
    run('rm -rf /data/web_static/releases/{}/web_static'.
        format(file_name.split('.')[0]))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ \
    /data/web_static/current'.format(file_name.split('.')[0]))
    print("New version deployed!")

    return True


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


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()

    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
