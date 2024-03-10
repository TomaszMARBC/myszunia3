import subprocess
from subprocess import CompletedProcess


class AccessError(Exception):
    """Exception for access error"""


def open_file(command: str) -> CompletedProcess:
    """Using the subprocess library to open system file.

    This function takes one parameter in str. Parameter is a path to folder and command to do.
    If everything goes well, function return completed process,
    otherwise function raise AccessError.
    
    Args:
        command: command to raise process.

    Returns:
        A CompletedProcess object representing the completed process.

    Raises
        AccessError: In case of a file access error.
    """
    try:
        execute_command = subprocess.run(command, capture_output=True, check=True, shell=True)
        return execute_command
    except subprocess.CalledProcessError as error:
        raise AccessError from error


# egzekwuje ścieżkę, pobiera info w bajtach, decoduje na utf-8 i z listy kolumn zwraca samą wartość:


mouse_file_path = r'HKEY_CURRENT_USER\Control Panel\Mouse'
settings_names = (
    'MouseSensitivity',
    'MouseSpeed',
    'MouseThreshold1',
    'MouseThreshold2',
    'MouseTrails'
)


def show_values(file_path: str, settings) -> tuple:
    mouse_settings = ()
    
    for setting in settings:
        cmd = f'REG QUERY "{file_path}" /v {setting}'
        result = open_file(cmd).stdout.decode('utf-8')
        
        if result.strip():
            mouse_settings += (result.strip().split()[-1],)
    
    return mouse_settings
