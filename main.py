import subprocess
import time

commands = [
r'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseSensitivity /t REG_SZ /d 20 /f',
r'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseSpeed /t REG_SZ /d 0 /f',
r'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseThreshold1 /t REG_SZ /d 0 /f',
r'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseThreshold2 /t REG_SZ /d 0 /f',
r'REG ADD "HKEY_CURRENT_USER\Control Panel\Mouse" /v MouseTrails /t REG_SZ /d 0 /f',
]

for i in range(len(commands)):
    cmd = subprocess.run(commands[i])
    time.sleep(1)