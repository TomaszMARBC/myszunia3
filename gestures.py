import pyautogui
import time

width, height = pyautogui.size()
"""Sprawdzamy szerokość i wysokość waszego monitora"""
half_width = 0.5 * width
half_height = 0.5 * height
"""dzielimy wartości na pół aby uzyskać cztery ćwiartki"""
print('Szerokość',width)
print('wysokość',height)

points = 0
start_time = time.time()
""" skrypt dowiaduje się która jest teraz godzina* """


anserws = set()
""" towrzymy set-a na odpowiedzi """
while (time.time() - start_time) < 4:
    """Ustawiamy licznik który będzie nam odmierzał 4 sekund, a później pętla się zakończy"""
    """Jeżeli zostanie spełniony warunek, czyli myszka znajdzie się w odpowiedniej ćwiartce, dodajemy punkt setowi """
    x,y = pyautogui.position()
    if x < half_width and y < half_height:
        #print('jesteś w pierwszej ćwiartce')
        anserws.add(1)
    if len(anserws) == 1:
        if x > half_width and y < half_height:
            #print('jesteś w drugiej ćwiartce')
            anserws.add(2)
    if len(anserws) ==2:
        if x > half_width and y > half_height:
            #print('jesteś w trzeciej ćwiartce')
            anserws.add(3)
    if len(anserws) == 3:
        if x < half_width and y > half_height:
            #print('jesteś w czwartej ćwiartce')
            anserws.add(4)
    if len(anserws) == 4:
        if x < half_width and y < half_height:
            #print('jesteś w pierwszej ćwiartce')
            anserws.add(5)
    
    if len(anserws) == 5:
        print('wykonałeś gest - zrobiłeś prawdopodobnie kółko')
        break