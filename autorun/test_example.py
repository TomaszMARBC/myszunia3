#  -*- coding: utf-8 -*-
''' Przykład wykorzystania funkcji z modułu autorun

Skrypt tworzy skrót w folderze Autostart do systemowego Notatnika.
Jeżeli skrót został poprawnie utworzony, to w terminalu pojawi się napis:

'Sprawdź obecność skrótu do pliku [ścieżka] w folderze Autostart: True'

Skrypt można uruchomić z parametrem 'del':
$ python text_example.py del
W tym trybie skrót do Notatnika powinien zostać usunięty.
W terminalu powinien pojawić się napis:
'Sprawdź obecność skrótu do pliku [ścieżka] w folderze Autostart: False'
'''

import os
import sys
import autorun as aur

TARGET = r'C:\Windows\System32\notepad.exe'

# utworzenie ścieżki skrótu do Notatnika w folderze autostart
shortcut_path = aur.create_shortcut_path(TARGET)

# sprawdzenie czy tryb usuwania skrótu jest włączony
if len(sys.argv) > 1:
    if sys.argv[1] == 'del':
        # usunięcie skrótu
        aur.delete_shortcut_from_startup(TARGET)
else:
    # utworzenei skrótu
    aur.create_starup_shortcut(TARGET)

# wyświetlenie komunikatu
print(
    f'Sprawdź obecność skrótu do pliku {TARGET} w folderze Autostart: ',
    os.path.exists(shortcut_path)
    )
