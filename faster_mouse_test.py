"""This tiny app increase speed of your mouse"""
import pyautogui
from time import sleep

str_how_much_faster = input("how many times faster do you want to go?")
how_much_faster = int(str_how_much_faster)
while True:
    x, y =pyautogui.position()
    sleep(0.001)
    x1, y1 = pyautogui.position()

    x2 = x1 - x
    xx = x2 * how_much_faster
    x3 = x1 + xx

    y2 = y1 - y
    yy = y2 * how_much_faster
    y3 = y1 + yy

    pyautogui.moveTo(x3, y3)

arkparks