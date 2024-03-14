"""Using the subprocess library to open system file."""

from itertools import zip_longest
import time
import subprocess_for_myszunia as myszunia
import user_input

if __name__ == '__main__':
    while True:
        mouse_file_path = r'HKEY_CURRENT_USER\Control Panel\Mouse'
        settings_names = (
            'MouseSensitivity',
            'MouseSpeed',
            'MouseThreshold1',
            'MouseThreshold2',
            'MouseTrails'
        )
        
        mouse_settings = myszunia.MouseSettings()
        
        current_settings = mouse_settings.show_values(mouse_file_path, settings_names)
        print(f'Bierzące ustawienia: {current_settings}')
        
        values_to_set = user_input.put_user_values(settings_names)
        
        mouse_settings.set_mouse_values(mouse_file_path, *values_to_set)
        time.sleep(2)
        entered_settings = mouse_settings.show_values(mouse_file_path, settings_names)
        
        values = zip_longest(settings_names, entered_settings)
        print('Aktualnie testowane ustawienia:\n')
        for name, value in values:
            print(f'Podana wartość: {name} = {value}')
    
        print(f'\nPowrót do poprzednich ustawień nastąpi za: 10s')
        time.sleep(10)
        mouse_settings.set_mouse_values(mouse_file_path, *current_settings)
        current_settings = mouse_settings.show_values(mouse_file_path, settings_names)
    
        print(f'Powrócono do ustawień początkowych: {current_settings}')
        
        choice = input(
            f'\n{'-' * 50}\n'
            f'Test zakończony.\n'
            f'Jeśli chcesz ponowić test i wprowadzić nowe wartości wciśnij Enter,\n'
            f'Jeśli chcesz wyjść z programu wpisz "q" i wciśnij Enter: '
        )
        if choice == 'q':
            break
        
