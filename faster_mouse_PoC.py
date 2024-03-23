"""This tiny app increase speed of your mouse"""
import pyautogui
import time

def main():
    str_how_much_faster = input('how fast your mouse should move? [1-30] -> ')
    how_much_faster = int(str_how_much_faster)
    start_time = time.time()
    min_movement = 3
    print('After 15 seconds, your setting will went back to defoult')
    while (time.time() - start_time) < 15:
        first_position_x , first_position_y =pyautogui.position()
        time.sleep(0.001)
        second_position_x, second_position_y = pyautogui.position()

        difference_x = second_position_x - first_position_x
        difference_y = second_position_y - first_position_y

        if abs(difference_x) >= min_movement or abs(difference_y) >= min_movement:
            distance_to_move_in_x = difference_x * how_much_faster
            third_position_x = second_position_x + distance_to_move_in_x
            distance_to_move_in_y = difference_y * how_much_faster
            third_position_y = second_position_y + distance_to_move_in_y


            pyautogui.moveTo(third_position_x, third_position_y)

if __name__=='__main__':
    main()