import pyautogui

"""Narazie będzie to działało tylko na komputerach z moją rozdzielczością monitora, ale już w krótce zrobię upgrade"""

print(pyautogui.size())
width, height = pyautogui.size()
print('szerokosc',width)
print('wysokosc',height)
pyautogui.moveTo(840,525)

points = 0
while True:
    x,y = pyautogui.position()
    if x < 840 and y < 525:
        print('jesteś w pierwszej ćwiartce')
    if x > 840 and y < 525:
        print('jesteś w drugiej ćwiartce')
    if x > 840 and y > 525:
        print('jesteś w trzeciej ćwiartce')
    if x < 840 and y > 525:
        print('jesteś w czwartej ćwiartce')