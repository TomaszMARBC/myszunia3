"""Using the subprocess library to open system file."""

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
        update_command = 'gpupdate /force'      # komenda wywołująca reload ustawień
        
        mouse_settings = myszunia.MouseSettings()
        
        print('Witamy w programie testującym ustawienia myszki\n\nOto bierzące ustawienia:')
        current_settings = mouse_settings.show_values(mouse_file_path, settings_names)
        print('\nProszę o wpisanie parametrów testu:')
        values_to_set = user_input.put_user_values(settings_names)
        test_time = user_input.set_time()
        
        print('Wprowadzam wartości testowe, może to chwilę potrwać.')
        mouse_settings.set_mouse_values(mouse_file_path, *values_to_set)
        mouse_settings.execute_command(update_command)   # robi reload ustawień nie wiem czy dotyczy myszki / długo trwa
        print('\nWartości testowe wprowadzone. \nZa chwilę rozpocznie się test da ustawień:\n')
        time.sleep(2)
        entered_settings = mouse_settings.show_values(mouse_file_path, settings_names)
        
        print(f'\nTest rozpoczęty.\nPowrót do poprzednich ustawień nastąpi za: {test_time}s')
        time.sleep(test_time)
        mouse_settings.set_mouse_values(mouse_file_path, *current_settings)
        
        print(f'\nPowrócono do ustawień początkowych:')
        mouse_settings.show_values(mouse_file_path, settings_names)
    
        choice = input(
            f'\n{'-' * 50}\n'
            f'Test zakończony.\n'
            f'Jeśli chcesz ponowić test i wprowadzić nowe wartości wciśnij Enter,\n'
            f'Jeśli chcesz wyjść z programu wpisz "q" i wciśnij Enter: '
        )
        if choice == 'q':
            break
        