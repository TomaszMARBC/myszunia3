import json
import subprocess
import os
from datetime import datetime


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
    
    with open(os.path.join(desktop_path, "pobrane_ustawienia_myszy.txt"), "a") as file:
        initial_settings = ()
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_time = f"\nData i czas zapisu: {current_datetime}\n"
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
                print(f'Wartość ustawienia dla {setting} = {value[0]}')
                
                file.write(file_content_values)
        file.write(str(initial_settings))
    
    # # Zapisanie listy do pliku JSON
    # with open(os.path.join(desktop_path, "kolejne_ustawienia_myszy.json"), "a") as json_file:
    #     json.dump(initial_settings, json_file)
