#  -*- coding: utf-8 -*-
'''Obsługa autostaru programu lub skryptu

Moduł zawiera funkcj: dodającą skrót do pliku w folderze Autostart (Startup)
oraz funkcję usuwającą skrót z tego folderu.
'''

import os
import win32com.client


def receive_user_autostart() -> str:
    """
    Zwraca ścieżkę do folderu, w którym znajdują się skróty programów
    uruchamianych automatycznie przy logowaniu użytkownika.

    Returns:
        str: Ścieżka do folderu uruchamiania automatycznego użytkownika.
    """
    # Zczytanie nazwy użytkownika komputera
    user_name = os.getenv("USERNAME")
    # ścieżka do folderu Startup
    startup_folder = f'C:\\Users\{user_name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    return startup_folder


def create_shortcut_path(target_path: str) -> str:
    """
    Tworzy ścieżkę do skrótu programu, który zostanie automatycznie uruchomiony
    przy logowaniu użytkownika.

    Args:
        target_path (str): Pełna ścieżka do pliku, którego skrót ma być utworzony.

    Returns:
        str: Ścieżka do utworzonego skrótu programu.

    Note:
        Funkcja ta zakłada, że target_path jest pełną ścieżką do pliku.

    Example:
        create_shortcut_path('C:\\Users\\User\\Desktop\\example.exe') => 
        'C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\example.lnk'
    """

    # Ścieżka do folderu Startup
    startup_folder = receive_user_autostart()
    # Wyodrębnienie nazwy pliku z target_path
    file_name = target_path.split('\\')[-1].split('.')[0]
    # Utworzenie nazwy skrótu
    shortcut_name = f'{file_name}.lnk'
    # Utworzenie ścieżki do skrótu w folderze Startup
    shortcut_path = os.path.join(startup_folder, shortcut_name)
    return shortcut_path


def create_starup_shortcut(target_path: str):
    '''
    Tworzy skrót programu w folderze uruchamiania automatycznego użytkownika.

    Args:
        target_path (str): Pełna ścieżka do pliku, którego skrót ma być utworzony.

    Note:
        Funkcja ta zakłada, że target_path jest pełną ścieżką do pliku.

    Example:
        create_starup_shortcut('C:\\Users\\User\\Desktop\\example.exe')
    '''
    # przygotowanie ścieżki do skrótu pliku
    shortcut_path = create_shortcut_path(target_path=target_path)
    # stworzenie skrótu
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.save()


def delete_shortcut_from_startup(target_path: str):
    '''
    Usuwa skrót programu z folderu uruchamiania automatycznego użytkownika.

    Args:
        target_path (str): Pełna ścieżka do pliku, którego skrót ma być usunięty.

    Note:
        Funkcja ta zakłada, że target_path jest pełną ścieżką do pliku.

    Example:
        delete_shortcut_from_startup('C:\\Users\\User\\Desktop\\example.exe')
    '''
    # przygotowanie ścieżki do skrótu pliku
    shortcut_path = create_shortcut_path(target_path=target_path)
    # usunięcie skrótu
    if os.path.isfile(shortcut_path):
        os.remove(shortcut_path)
    else:
        print(f'Brak skrótu {shortcut_path}')
