from itertools import zip_longest

settings_names = (
    'MouseSensitivity',
    'MouseSpeed',
    'MouseThreshold1',
    'MouseThreshold2',
    'MouseTrails'
)


def put_user_values():
    choices = {'y', 'Y', 'Yes', 'yes'}
    
    while True:
        user_values = ()
        
        for name in settings_names:
            user_input = input(f'Podaj wartość {name}: ')
            
            if user_input.isdigit():
                user_values += (user_input,)
        
        print('-' * 50 + '\n')
        values = zip_longest(settings_names, user_values)
        for name, value in values:
            print(f'Podana wartość: {name} -> {value}')
        
        user_choice = input(
            f'Jeśli chcesz wprowadzić wartości ponownie, wpisz "yes", w przeciwnym wypadku naciśnij Enter: ')
        
        if user_choice.lower() not in choices:
            break
    
    return user_values
#
#

