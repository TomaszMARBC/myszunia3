"""Using the subprocess library to open system file."""

import subprocess
from subprocess import CompletedProcess


class AccessError(Exception):  # TODO dodaj więcej exceptions docstringi i testy
    """Exception for access error"""


class MouseSettings:        # TODO dodaj logi
    def __init__(self) -> None:
        self.command = None
        self.file_path = None
        self.current_values = None
        self.settings_names = None
    
    @staticmethod
    def execute_command(command: str) -> CompletedProcess:
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
            execute_command = subprocess.run(command, capture_output=True, check=True, shell=True)
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
        self.current_values = ()
        
        for setting in self.settings_names:
            command = f'REG QUERY "{file_path}" /v {setting}'
            result = self.execute_command(command).stdout.decode('utf-8')
            
            if result.strip():
                self.current_values += (result.strip().split()[-1],)
        
        return self.current_values
    
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
            'MouseSensitivity': sensitivity,
            'MouseSpeed': speed,
            'MouseThreshold1': treshold1,
            'MouseThreshold2': treshold2,
            'MouseTrails': trails
        }
        
        for setting, value in set_mouse_settings.items():
            command = f'REG ADD "{file_path}" /v {setting} /t REG_SZ /d {value} /f'
            self.execute_command(command)
