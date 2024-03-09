"""This tiny app increase speed of your mouse"""
import pyautogui
import time

def main():
    str_how_much_faster = 25
    how_much_faster = int(str_how_much_faster)
    start_time = time.time()
    min_movement = 3

    while (time.time() - start_time) < 30:
        x, y =pyautogui.position()
        time.sleep(0.001)
        x1, y1 = pyautogui.position()

        difference_x = x1 - x
        difference_y = y1 - y

        if abs(difference_x) >= min_movement or abs(difference_y) >= min_movement:
            xx = difference_x * how_much_faster
            x3 = x1 + xx
            yy = difference_y * how_much_faster
            y3 = y1 + yy


            pyautogui.moveTo(x3, y3)

if __name__=='__main__':
    main()