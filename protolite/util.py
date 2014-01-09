import os


def abs_path(path):
    path = os.path.expanduser(path)
    path = os.path.abspath(path)
    path = os.path.realpath(path)
    path = os.path.normpath(path)
    return path
