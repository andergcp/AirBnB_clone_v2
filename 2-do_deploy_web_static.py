#!/usr/bin/python3
from fabric.api import *
from os import path

env.hosts = [
    '34.74.122.27',
    '35.243.238.143'
]

env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not path.isfile(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    remote_path = "/tmp/{}".format(file_name)

    put(archive_path, remote_path)
    run('mkdir -p /data/web_static/releases/{}/'.format(file_name))
    run('tar -xzf /tmp/{0} -C\
    /data/web_static/releases/{0}/'.format(file_name))
    run('rm /tmp/{}'.format(file_name))
    run('mv /data/web_static/releases/{0}/web_static/* \
    /data/web_static/releases/{0}/'.format(file_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(file_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ \
    /data/web_static/current'.format(file_name))
    print("New version deployed!\n")
