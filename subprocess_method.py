"""Using the subprocess library to open system file."""

import subprocess
from subprocess import CompletedProcess
import time
import initial_mouse_settings as mouse

if __name__ == '__main__':
    
    class AccessError(Exception):                   # TODO dodaj więcej exceptions docstringi i testy
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
    
    
    def set_mouse_values(
            reg_path: str,
            sensitivity: int,
            speed: int,
            treshold1: int,
            treshold2: int,
            trails: int
    ) -> None:
        """Sets mouse-related settings in the Windows registry.

            Args:
                reg_path (str): The registry path where the settings should be modified.
                sensitivity (int): The sensitivity value for the mouse.
                speed (int): The speed value for the mouse.
                treshold1 (int): The threshold 1 value for the mouse.
                treshold2 (int): The threshold 2 value for the mouse.
                trails (int): The trails value for the mouse.

            Returns:
                None

            Raises:
                Any exceptions that occur during the registry modification process.

            Note:
                This function modifies the Windows registry. Use with caution.
            """
        mouse_settings = {
            'mouse_sensitivity': sensitivity,
            'mouse_speed': speed,
            'mouse_treshold1': treshold1,
            'mouse_treshold2': treshold2,
            'mouse_trails_cmd': trails
        }
        
        for setting, value in mouse_settings.items():
            cmd = f'REG ADD "{reg_path}" /v {setting} /t REG_SZ /d {value} /f'
            open_file(cmd)
    
    
    mouse_file_path = r'HKEY_CURRENT_USER\Control Panel\Mouse'
    initial_mouse_settings = mouse.show_values(mouse_file_path, mouse.settings_names)
    test_values = (100, 10, 0, 0, 0)
    
    print(f'Pierwotne wartości myszki: {initial_mouse_settings}\nZmieniam na {test_values}')
    
    set_mouse_values(mouse_file_path, *test_values)
    current_values = mouse.show_values(mouse_file_path, mouse.settings_names)
    print(f'Aktualne ustawienia: {current_values}')
    print(f'\nZmiana ustawień myszki zakończona sukcesem.\n{'*' * 50} ')        # TODO dodaj logi zamiast printów
    time.sleep(30)
    
    print(f'Przywracam pierwotne wartości myszki: {initial_mouse_settings}')
    set_mouse_values(mouse_file_path, *initial_mouse_settings)
    
    print(f'\nZmiana ustawień myszki zakończona sukcesem.\n{'*' * 50}')
