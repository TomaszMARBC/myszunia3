"""Using the subprocess library to open system file."""

import time
import subprocess_for_myszunia as myszunia
import user_input

if __name__ == '__main__':
    
    mouse_file_path = r'HKEY_CURRENT_USER\Control Panel\Mouse'
    settings_names = (
        'MouseSensitivity',
        'MouseSpeed',
        'MouseThreshold1',
        'MouseThreshold2',
        'MouseTrails'
    )
    
    mouse_settings = myszunia.MouseSettings()  # TODO dodaj ładne wyświetlanie ustawienia -> wartości
    
    current_settings = mouse_settings.show_values(mouse_file_path, settings_names)
    print(f'Bierzące ustawienia: {current_settings}')
    
    values_to_set = user_input.put_user_values()
    print("Ostateczne wartości:", values_to_set)
    
    mouse_settings.set_mouse_values(mouse_file_path, *values_to_set)
    time.sleep(2)
    entered_settings = mouse_settings.show_values(mouse_file_path, settings_names)
    print(f'Ustawienia po zmianie: {entered_settings}')

    print(f'Powrót do poprzednich ustawień nastąpi za: 10s')
    time.sleep(10)
    mouse_settings.set_mouse_values(mouse_file_path, *current_settings)
    current_settings = mouse_settings.show_values(mouse_file_path, settings_names)
    print(f'Bierzące ustawienia: {current_settings}')
    
