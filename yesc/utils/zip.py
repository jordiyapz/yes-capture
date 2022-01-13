import typing
import zipfile
import os


def unzip_all(zip_filepath: os.PathLike, target_filepath: os.PathLike, **kwargs):
    with zipfile.ZipFile(zip_filepath, 'r', **kwargs) as zip_ref:
        zip_ref.extractall(target_filepath)
