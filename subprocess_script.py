"""Using the subprocess library to open system file."""

from pathlib import Path
import subprocess


class AccessError(Exception):
    """Exception for access error"""


def path_converter(path) -> str:
    """
    Converts given path to the str of path object using the library pathlib.
    
    :param path: Path to conversion.
    :return: a str type of Path object.
    """
    str_path = str(Path(path))

    return str_path


def open_file(path):
    """
    Using the subprocess library to open system file.
    
    :param path: Path to system file.
    :type path: str
    :return: A CompletedProcess object representing the completed process.
    :rtype: subprocess.CompletedProcess
    :raises AccessError: In case of a file access error.
    """
    try:
        myszunio_lec = subprocess.run(path, check=True, shell=True)
        return myszunio_lec
    except subprocess.CalledProcessError as error:
        raise AccessError from error


FILE_PATH = r'C:\WINDOWS\regedit.exe'
# TEST_PATH = r'regedit /s HKEY_CURRENT_USER\Control Panel\Mouse\MouseSensitivity.reg'
# NOWA_PATH = r'reg add HKEY_CURRENT_USER\Control Panel\Mouse /v MouseSensitivity /t REG_SZ /d 5 /f'

open_file(path_converter(FILE_PATH))
