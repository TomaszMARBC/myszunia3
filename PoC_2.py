"""This tiny app increase speed of your mouse"""
import pyautogui
import time
import os


def collecting_data():
    """
    Function to collect user input for mouse movement speed and record start time.

    Returns:
        tuple: A tuple containing start time (float) and mouse movement speed (int).
    pi
    Raises:
        ValueError: If the input for mouse movement speed is not an integer.
    """
    str_how_much_faster = 8
    how_much_faster = float(str_how_much_faster)
    start_time = time.time()
    return start_time, how_much_faster

def PyAutoGUI_Movement(how_much_faster):
    """
    Moves the mouse cursor with PyAutoGUI library while considering the speed factor.

    Args:
        how_much_faster (int): Factor to adjust the speed of mouse movement.

    Notes:
        This function calculates the difference between two consecutive mouse positions,
        then moves the mouse cursor according to the provided speed factor.

    Parameters:
        how_much_faster (int): A positive integer representing the speed factor. 
            Higher values result in faster mouse movement.

    Raises:
        None

    Returns:
        None
    """
    first_position_x , first_position_y =pyautogui.position()
    second_position_x, second_position_y = pyautogui.position()

    difference_x = second_position_x - first_position_x
    difference_y = second_position_y - first_position_y

    if abs(difference_x) >= 30 or abs(difference_y) >= 30:
        distance_to_move_in_x = difference_x * how_much_faster
        third_position_x = second_position_x + distance_to_move_in_x
        distance_to_move_in_y = difference_y * how_much_faster
        third_position_y = second_position_y + distance_to_move_in_y


        pyautogui.moveTo(third_position_x, third_position_y)


def main():
    pyautogui.FAILSAFE = False
    
    start_time, how_much_faster = collecting_data()
    
    print('Aby zakończyć - wyłącz program')
    
    while True:
        PyAutoGUI_Movement(how_much_faster)

        

if __name__=='__main__':
    main()