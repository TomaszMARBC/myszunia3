"""Using the subprocess library to open system file."""     # TODO sprawdzić komentarze na git hubie

import subprocess                                           # TODO dodaj if __name__ == __main__
from subprocess import CompletedProcess


class AccessError(Exception):
    """Exception for access error"""


def open_file(path: str, command: str) -> CompletedProcess:   # TODO zmienić docstringi na google style python docstring
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
        zmien_wartosc = subprocess.run(path + command, check=True)
        return zmien_wartosc
    except subprocess.CalledProcessError as error:
        raise AccessError from error


# komendy które będziemy wywoływać:                                         # TODO wywalić do funkcji/ yaml

MOUSE_FILE_PATH = r'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse"'        # TODO zmienić znaki na lowercase pozniej

MOUSE_SENSITIVITY_COMMAND = r' /v MouseSensitivity /t REG_SZ /d 10 /f'  # 10 - wartosci przed zmianami
MOUSE_SPEED = r' /v MouseSpeed /t REG_SZ /d 0 /f'  # 1
MOUSE_TRESHOLD1 = r' /v MouseThreshold1 /t REG_SZ /d 0 /f'  # 6
MOUSE_TRESHOLD2 = r' /v MouseThreshold2 /t REG_SZ /d 0 /f'  # 10
MOUSE_TRAILS = r' /v MouseTrails /t REG_SZ /d 0 /f'  # 0

commands = (
    MOUSE_SENSITIVITY_COMMAND,
    MOUSE_SPEED,
    MOUSE_TRESHOLD1,
    MOUSE_TRESHOLD2,
    MOUSE_TRAILS
)

for command in commands:        # TODO jak się przeliterować po tupli?
    open_file(MOUSE_FILE_PATH, command)
    
print('Zmiana ustawień myszki zakończona sukcesem.')
