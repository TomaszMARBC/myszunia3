"""Using input function to set test values """

from itertools import zip_longest


def put_user_values(settings_names: tuple[str, ...]) -> tuple[str, ...]:
    """
    Retrieves values from the user for the provided settings.
    
    In the loop, the user is presented with subsequent names of the settings from `settings_names`.
    The user provides values for each name. If an incorrect value is provided
     (which is not a number), the user is asked to enter the number again.
    After providing all the values, the program presents the given values for verification.
    The user has the option of re-entering the value or ending the function.

    Args:
        settings_names (Tuple[str]): A tuple of the names of the settings for which the user provides values.

    Returns:
        Tuple[str]: A tuple of user-supplied values.
    """
    
    while True:
        user_values = ()
        
        for name in settings_names:
            user_input = input(f'Podaj wartość {name}: ')
            
            while True:
                if user_input.isdigit():
                    user_values += (user_input,)
                    break
                else:
                    user_input = input(f'Podaj wartość liczbową {name}: ')
        
        print('-' * 50 + '\n')
        values = zip_longest(settings_names, user_values)
        for name, value in values:
            print(f'Podana wartość: {name} = {value}')
        
        user_choice = input(
            f'\nJeśli chcesz wprowadzić wartości ponownie, wpisz "y" i wciśnij Enter\n'
            f'Jeśi chcesz rozpocząć test wciśnij Enter: ')
        
        if user_choice != 'y':
            break
    
    return user_values


def set_time() -> int:
    """
    Retrieves value from the user.
    
    Returns:
        int: A integer of user-supplied value.
    
    """
    user_time = input('Podaj czas trwania testu w sekundach: ')
    while True:
        if user_time.isdigit():
            break
        else:
            user_time = input('Wpisz liczbę sekund: ')
    return int(user_time)
