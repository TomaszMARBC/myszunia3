"""Using the subprocess library to open system file."""

import subprocess
from subprocess import CompletedProcess


class AccessError(Exception):  # TODO dodaj więcej exceptions docstringi i testy
    """Exception for access error"""


class MouseSettings:        # TODO dodaj logi
    def __init__(self) -> None:
        self.command = None
        self.file_path = None
        self.mouse_settings = None
        self.settings_names = None
    
    def execute_command(self) -> CompletedProcess:
        """
        Using the subprocess library to open system file.

            This function takes one parameter in str. Parameter is a path to folder and command to do.
            If everything goes well, function return completed process,
            otherwise function raise AccessError.

            Args:
                self.command: command to raise process.

            Returns:
                A CompletedProcess object representing the completed process.

            Raises
                AccessError: In case of a file access error.
        """
        try:
            execute_command = subprocess.run(self.command, capture_output=True, check=True, shell=True)
            return execute_command
        except subprocess.CalledProcessError as error:
            raise AccessError from error
    
    # TODO popraw funkcję by zwracała bierzące ustawienia a nie z pamięci ->
    def show_values(self, file_path: str, settings_names: tuple) -> tuple:
        """
        Retrieves the values of specified settings from the Windows registry.

        Args:
            file_path (str): The registry path to query.
            settings_names (tuple): A tuple of setting names to retrieve.

        Returns:
            tuple: A tuple containing the values of the specified settings.
        """
        self.settings_names = settings_names
        self.mouse_settings = ()
        
        for setting in self.settings_names:
            self.command = f'REG QUERY "{file_path}" /v {setting}'
            result = self.execute_command().stdout.decode('utf-8')
            
            if result.strip():
                self.mouse_settings += (result.strip().split()[-1],)
        
        return self.mouse_settings
    
    def set_mouse_values(
            self,
            file_path: str,
            sensitivity: int,
            speed: int,
            treshold1: int,
            treshold2: int,
            trails: int
    ) -> None:
        """
        Sets mouse-related settings in the Windows registry.

        Args:
            file_path (str): The registry path where the settings should be modified.
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
        set_mouse_settings = {
            'mouse_sensitivity': sensitivity,
            'mouse_speed': speed,
            'mouse_treshold1': treshold1,
            'mouse_treshold2': treshold2,
            'mouse_trails_cmd': trails
        }
        
        for setting, value in set_mouse_settings.items():
            self.command = f'REG ADD "{file_path}" /v {setting} /t REG_SZ /d {value} /f'
            self.execute_command()
    

mouse_file_path = r'HKEY_CURRENT_USER\Control Panel\Mouse'
settings_names = (
    'MouseSensitivity',
    'MouseSpeed',
    'MouseThreshold1',
    'MouseThreshold2',
    'MouseTrails'
)
test_values = (100, 10, 0, 0, 0)

# happy testing
mouse_settings = MouseSettings()        # TODO dodaj ładne wyświetlanie ustawienia -> wartości
print(f'Ustawienia początkowe: {mouse_settings.show_values(mouse_file_path, settings_names)}')
mouse_settings.set_mouse_values(mouse_file_path, *test_values)
print(f'Ustawienia po zmianie: {mouse_settings.show_values(mouse_file_path, settings_names)}')

