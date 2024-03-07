import os
from autorun import create_starup_shortcut


target = r'C:\Windows\System32\notepad.exe'
create_starup_shortcut(target)

user_name = os.getenv("USERNAME")
startup_path = f'C:\\Users\{user_name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\notepad.lnk'

print(
    f'Sprawdź obecność skrótu do pliku {target} w folderze Autostart: ',
    os.path.exists(startup_path)
    )
