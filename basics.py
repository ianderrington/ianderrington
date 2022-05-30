Basic functions 


import contextlib
import json
import os
import shutil
import tempfile

import tensorflow as tf
import yaml


def _check_parent_dir_exists(path):
    dir_path = os.path.dirname(os.path.abspath(path))
    if not tf.io.gfile.exists(dir_path):
        tf.io.gfile.makedirs(dir_path)


def dump_yaml(target_path, data):
    dir_path = os.path.dirname(os.path.abspath(target_path))
    if not tf.io.gfile.exists(dir_path):
        tf.io.gfile.makedirs(dir_path)
    with tf.io.gfile.GFile(target_path, 'w') as stream:
        yaml.dump(data, stream=stream)


class FileHandler(object):
    def load(self, file_path):
        with tf.io.gfile.GFile(file_path) as stream:
            parsed = self._load(stream)
        return parsed

    def _load(self, stream):
        raise NotImplementedError()

    def dump(self, file_path, data):
        _check_parent_dir_exists(file_path)
        with tf.io.gfile.GFile(file_path, 'w') as stream:
            self._dump(stream, data)

    def _dump(self, stream, data):
        raise NotImplementedError()


class YamlHandler(FileHandler):
    def _load(self, stream):
        return yaml.safe_load(stream)

    def _dump(self, stream, data):
        yaml.dump(data, stream=stream)


class JsonHandler(FileHandler):
    def _load(self, stream):
        return json.load(stream)

    def _dump(self, stream, data):
        json.dump(data, stream, indent=4)


def handler_factory(extension):
    if extension in {'.yml', '.yaml'}:
        return YamlHandler()

    elif extension == '.json':
        return JsonHandler()

    else:
        raise ValueError('Unsupported file type {}.'.format(extension))


def get_extension(file_path):
    return os.path.splitext(file_path)[1]


def load(file_path):
    handler = handler_factory(get_extension(file_path))
    return handler.load(file_path)


def dump(file_path, data):
    handler = handler_factory(get_extension(file_path))
    return handler.dump(file_path, data=data)


@contextlib.contextmanager
def directory_context(dir_path=None):
    """Context used to manage directory. If no directory is provided, one temporary directory will
    be generated and later on deleted. If a directory is provided, it will be preserved later.

    Args:
        dir_path: `str`, default to `None` to generate temporary directory.

    Yields:
        `str`, the path to a directory

    """
    if dir_path is None:
        dir_path = tempfile.mkdtemp()
        dir_provided = False
    else:
        dir_provided = True
    yield dir_path
    if not dir_provided:
        shutil.rmtree(dir_path)

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

