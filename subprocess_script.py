"""Using the subprocess library to open system file."""

from pathlib import Path
import subprocess


class AccessError(Exception):
    """Exception for access error"""


def path_converter(path) -> str:
    """
    Converts given path to the str of path object using the library pathlib.
    
    :param path: Path to conversion.
    :return: str of Path object.
    """
    str_path = str(Path(path))

    return str_path


def open_file(path):
    """
    Using the subprocess library to open system file.
    
    :param path: Path to system file.
    :type path: str
    :argument: Run function path_converter().
    :return: A CompletedProcess object representing the completed process.
    :rtype: subprocess.CompletedProcess
    :raises AccessError: In case of a file access error.
    """
    try:
        myszunio_lec = subprocess.run(path_converter(path), check=True, shell=True)
        return myszunio_lec
    except subprocess.CalledProcessError as error:
        raise AccessError from error


FILE_PATH = r'C:\WINDOWS\regedit.exe'

open_file(FILE_PATH)
