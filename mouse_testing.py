from pynput.mouse import Button, Controller
"""pierwsze musimy zainstalować 'pip install pynput' """

mouse = Controller()

#print(mouse.position)
"""drukuje nam aktualną pozycje myszki"""
# mouse.position = (10,20)
"""ustawia myszke na pozycji o podanych koordynatach"""

# if mouse.position == (10,20):
#     print('wykryło myszkę')
# else:
#     print('myszka jest gdzieś indziej')
"""Prosta sekwencja która działa.
sprawdza czy myszka jest we wskazanym miejscu"""

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import pyautogui
"""pierwsze musimy zainstalować 'pip install pyautogui' """

print(pyautogui.size())
"""Drukuje wielkość ekranu"""
print(pyautogui.position())
"""Drukuje aktualne położenie myszki"""

#print(pyautogui.mouseInfo())
"""Odpala mini program który
Pokazuje absurdalnie dużo przydatnych informacji o myszcze, i ma wbudowaną funkcjonalność
przechwytuje nie tylko pozycje ale również można tym zrobić screnshoot-a"""

#pyautogui.moveTo(300,300,duration=3)
"""
dzięki tej komendzie myszka zmieni nam pozycje na 300x300 z prędkością 3
im większa wartość duration tym wolniej
wartość durration jest nie obowiązkowa
"""
