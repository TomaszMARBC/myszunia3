"""This tiny app increase speed of your mouse"""
import pyautogui
import time
import os

def collecting_data():
    """
    Function to collect user input for mouse movement speed and record start time.

    Returns:
        tuple: A tuple containing start time (float) and mouse movement speed (int).
    
    Raises:
        ValueError: If the input for mouse movement speed is not an integer.
    """
    str_how_much_faster = input('how fast your mouse should move? [1-30] -> ')
    str_min_movement = input('what is the speed limit, for mouse without extra superpower? [5-30] -> ')
    min_movement = int(str_min_movement)
    how_much_faster = int(str_how_much_faster)
    start_time = time.time()
    return start_time, how_much_faster, min_movement

def PyAutoGUI_Movement(how_much_faster, min_movement):
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
    
    if abs(difference_x) >= min_movement or abs(difference_y) >= min_movement:
        distance_to_move_in_x = difference_x * how_much_faster
        third_position_x = second_position_x + distance_to_move_in_x
        distance_to_move_in_y = difference_y * how_much_faster
        third_position_y = second_position_y + distance_to_move_in_y


        pyautogui.moveTo(third_position_x, third_position_y)

def looking_for_best_solution():
    """
    Function to interactively adjust mouse movement speed based on user feedback.

    This function prompts the user to provide feedback on the mouse movement. If the user
    likes the current speed, it continues moving the mouse at that speed until manually
    stopped. If the user does not like it, it prompts for new input and adjusts the speed
    accordingly.

    Args:
        None

    Raises:
        ValueError: If the input for mouse movement speed is not an integer.

    Returns:
        None
    """
    what_next = input('did you liked that? [y/n]: ')

    if what_next == 'y':
        os.system('cls')
        print('Then - that will work as long as you wont turn it off')
        str_how_much_faster = input('Once again, how fast it should be? [1-30] -> ')
        how_much_faster = int(str_how_much_faster)
        str_min_movement = input('what is the speed limit, for mouse without extra superpower? [5-30] -> ')
        min_movement = int(str_min_movement)
        while True:
            PyAutoGUI_Movement(how_much_faster, min_movement)
    else:
        print("let's give it another try...")
        time.sleep(1)
        start_time, how_much_faster, min_movement = collecting_data()
        while (time.time() - start_time) < 15:
            PyAutoGUI_Movement(how_much_faster, min_movement)    

def main():
    pyautogui.FAILSAFE = False
    
    start_time, how_much_faster, min_movement = collecting_data()
    
    print('After 15 seconds, your settings will went back to default')
    
    while (time.time() - start_time) < 15:
        PyAutoGUI_Movement(how_much_faster, min_movement)

    while True:
        looking_for_best_solution()

        

if __name__=='__main__':
    main()