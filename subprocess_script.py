"""Using the subprocess library to open system file."""

from pathlib import Path
import subprocess
from subprocess import CompletedProcess


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


def open_file(path: str, command: str) -> CompletedProcess:
    """
    Using the subprocess library to open system file.
    
    :param path: Path to system file.
    :param command: command to raise process
    :type path: str
    :return: A CompletedProcess object representing the completed process.
    :rtype: subprocess.CompletedProcess
    :raises AccessError: In case of a file access error.
    """
    try:
        myszuniu_lec = subprocess.run(path + command, check=True)
        return myszuniu_lec
    except subprocess.CalledProcessError as error:
        raise AccessError from error


MOUSE_FILE_PATH = r'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse"'
MOUSE_SENSITIVITY_COMMAND = r' /v MouseSensitivity /t REG_SZ /d 20 /f'

open_file(path_converter(MOUSE_FILE_PATH), MOUSE_SENSITIVITY_COMMAND)
