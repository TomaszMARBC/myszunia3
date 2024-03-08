"""The script responsible for performing gestures"""
import pyautogui
import time


def main():
    width, height = pyautogui.size()
    """We check the width and height of your monitor"""
    half_width = 0.5 * width
    half_height = 0.5 * height
    """We divide the values ​​in half to get four quarters"""

    points = 0
    start_time = time.time()
    """ the script finds out what time it is now """


    anserws = set()
    """ we create a set for answers """
    print('wykonaj gest.')
    while (time.time() - start_time) < 4:
        """We set a counter that will count down 4 seconds, and then the loop will end"""
        """If the condition that the mouse is in the appropriate quarter is met, we add a point to the set"""
        x,y = pyautogui.position()
        if x < half_width and y < half_height:
            anserws.add(1)
        if len(anserws) == 1:
            if x > half_width and y < half_height:
                anserws.add(2)
        if len(anserws) ==2:
            if x > half_width and y > half_height:
                anserws.add(3)
        if len(anserws) == 3:
            if x < half_width and y > half_height:
                anserws.add(4)
        if len(anserws) == 4:
            if x < half_width and y < half_height:
                anserws.add(5)
        
        if len(anserws) == 5:
            print('wykonałeś gest - zrobiłeś prawdopodobnie kółko')
            break
if __name__ == '__main__':
    main()