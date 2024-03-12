"""Using the subprocess library to open system file."""

import time
import subprocess_for_myszunia as myszunia

if __name__ == '__main__':
    
    # TODO napisz funkcję przyjmującą rządane ustawienia myszki
    user_values = ()
    def put_user_values(user_values):
        user_values += input()
        return user_values
    
    while len(user_values) < 5:

        print(
            'Podaj kolejno wartości dla następujacych ustawień:\n',
            'MouseSensitivity\n',
            'MouseSpeed\n',
            'MouseThreshold1\n',
            'MouseThreshold2\n',
            'MouseTrails'
            )
        put_user_values(user_values)
    
    mouse_file_path = r'HKEY_CURRENT_USER\Control Panel\Mouse'
    settings_names = (
        'MouseSensitivity',
        'MouseSpeed',
        'MouseThreshold1',
        'MouseThreshold2',
        'MouseTrails'
    )
    test_values = (100, 50, 0, 0, 0)
    
    # happy testing
    mouse_settings = myszunia.MouseSettings()  # TODO dodaj ładne wyświetlanie ustawienia -> wartości
    
    current_settings = mouse_settings.show_values(mouse_file_path, settings_names)
    print(f'Bierzące ustawienia: {current_settings}')
    
    mouse_settings.set_mouse_values(mouse_file_path, *test_values)      # TODO nie podaje test values!!!
    time.sleep(2)
    entered_settings = mouse_settings.show_values(mouse_file_path, settings_names)
    print(f'Ustawienia po zmianie: {entered_settings}')

    print(f'Powrót do poprzednich ustawień nastąpi za: 10s')
    time.sleep(10)
    mouse_settings.set_mouse_values(mouse_file_path, *current_settings)
    current_settings = mouse_settings.show_values(mouse_file_path, settings_names)
    print(f'Bierzące ustawienia: {current_settings}')
    
