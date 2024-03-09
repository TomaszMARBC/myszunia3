"""Using the subprocess library to open system file."""

import subprocess
from subprocess import CompletedProcess

if __name__ == '__main__':

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
            change_value = subprocess.run(command, check=True)
            return change_value
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
    test_values = (10, 1, 0, 0, 0)
    set_mouse_values(mouse_file_path, *test_values)
    
    print(f'\n{'*' * 30} \nZmiana ustawień myszki zakończona sukcesem.')
