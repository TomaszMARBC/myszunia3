import os
import win32com.client

def create_starup_shortcut(target_path: str):
    '''
    Funkcja tworzy skrót do pliku w folderze Startup (Autostart).
    Jako argument przyjmowany jest string ze ścieżką dostępu do pliku.
    '''
    # zczytanie nazwy użytkownika
    user_name = os.getenv("USERNAME")
    # przygotowanie ścieżki do skrótu pliku
    file_name = target_path.split('\\')[-1].split('.')[0]
    shortcut_name = f'{file_name}.lnk'
    startup_folder = f'C:\\Users\{user_name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    shortcut_path = os.path.join(startup_folder, shortcut_name)
    # stworzenie skrótu
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.save()
