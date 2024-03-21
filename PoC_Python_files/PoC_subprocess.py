"""Using the subprocess library to open system file."""

from datetime import datetime
from itertools import zip_longest
import os
import subprocess
from subprocess import CompletedProcess
import time


class AccessError(Exception):
    """Exception for access error"""


class MouseSettings:
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
                value = (result.strip().split()[-1],)
                self.current_values += value
                print(f'Wartość ustawienia dla {setting} = {value[0]}')
        
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

##############################################################


def put_user_values(settings_names: tuple[str, ...]) -> tuple[str, ...]:
    """
    Retrieves values from the user for the provided settings.

    In the loop, the user is presented with subsequent names of the settings from `settings_names`.
    The user provides values for each name. If an incorrect value is provided
     (which is not a number), the user is asked to enter the number again.
    After providing all the values, the program presents the given values for verification.
    The user has the option of re-entering the value or ending the function.

    Args:
        settings_names (Tuple[str]): A tuple of the names of the settings for which the user provides values.

    Returns:
        Tuple[str]: A tuple of user-supplied values.
    """
    
    while True:
        user_values = ()
        
        for name in settings_names:
            user_input = input(f'Podaj wartość {name}: ')
            
            while True:
                if user_input.isdigit():
                    user_values += (user_input,)
                    break
                else:
                    user_input = input(f'Podaj wartość liczbową {name}: ')
        
        print('-' * 50 + '\n')
        values = zip_longest(settings_names, user_values)
        for name, value in values:
            print(f'Podana wartość: {name} = {value}')
        
        user_choice = input(
            f'\nJeśli chcesz wprowadzić inne wartości, wpisz -> "y" i wciśnij Enter\n'
            f'Jeśi chcesz wgrać podane wartości -> wciśnij Enter: ')
        
        if user_choice != 'y':
            break
    
    return user_values


def set_time() -> int:
    """
    Retrieves value from the user.

    Returns:
        int: A integer of user-supplied value.

    """
    user_time = input('Podaj czas trwania testu w sekundach: ')
    while True:
        if user_time.isdigit():
            break
        else:
            user_time = input('Wpisz liczbę sekund: ')
    return int(user_time)


if __name__ == '__main__':
    mouse_file_path = r'HKEY_CURRENT_USER\Control Panel\Mouse'
    settings_names = (
        'MouseSensitivity',
        'MouseSpeed',
        'MouseThreshold1',
        'MouseThreshold2',
        'MouseTrails'
    )
    
    commands = (
        r'REG QUERY "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseSensitivity',
        r'REG QUERY "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseSpeed',
        r'REG QUERY "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseThreshold1',
        r'REG QUERY "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseThreshold2',
        r'REG QUERY "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseTrails'
    )
    
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    print('\nWitamy w programie testującym ustawienia myszki.\n')
    
    with open(os.path.join(desktop_path, "pobrane_ustawienia_myszy.txt"), "a") as file:
        initial_settings = ()
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_time = f"\n\nData i czas zapisu: {current_datetime}\n"
        file.write(save_time)
        
        for setting in settings_names:
            command = f'REG QUERY "{mouse_file_path}" /v {setting}'
            command_result = subprocess.run(command, capture_output=True, check=True, shell=True)
            result = command_result.stdout.decode('utf-8')
            
            if result.strip():
                value_str = result.strip().split()[-1]
                value_int = int(value_str)
                value = (value_int,)
                initial_settings += value
                
                file_content_values = f"{setting} = {result.strip().split()[-1]}\n"
                # print(f'Wartość ustawienia dla {setting} = {value[0]}')
                
                file.write(file_content_values)
        file.write(str(initial_settings))
        print(f'Aktualne ustawienia zostały zapisane w pliku "pobrane_ustawienia_myszy.txt" na Twoim pulpicie\n')
    
    while True:
        mouse_file_path = r'HKEY_CURRENT_USER\Control Panel\Mouse'
        settings_names = (
            'MouseSensitivity',
            'MouseSpeed',
            'MouseThreshold1',
            'MouseThreshold2',
            'MouseTrails'
        )
        
        mouse_settings = MouseSettings()
        
        print('Oto bierzące ustawienia:')
        current_settings = mouse_settings.show_values(mouse_file_path, settings_names)
        print('\nProszę o wpisanie parametrów testu:')
        values_to_set = put_user_values(settings_names)
        
        print('Wprowadzam wartości testowe, może to chwilę potrwać.')
        mouse_settings.set_mouse_values(mouse_file_path, *values_to_set)
        time.sleep(2)
        print('\nZostały wprowadzone następujące wartości: \n')
        entered_settings = mouse_settings.show_values(mouse_file_path, settings_names)
        
        choice = input(
            f'\n{'-' * 50}\n'
            f'Wprowadzanie zakończone.\n\n'
            f'Wymagane ponowne uruchomienie systemu operacyjnego.\n\n'
            f'Jeśli chcesz wprowadzić inne wartości wciśnij -> Enter,\n'
            f'Jeśli chcesz uruchomić ponownie komputer wpisz -> "y" i wciśnij Enter\n'
            f'Jeśli chcesz wyjść z programu wpisz -> "q" i wciśnij Enter: '
        )
        if choice == 'q':
            break
        elif choice == 'y':
            update_command = 'shutdown /r /t 2'
            mouse_settings.execute_command(update_command)
        