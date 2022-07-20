from .constants import CONSTANTS
from .dictionaries import DICTIONARIES
from .length import convert as convert_length
from .time import convert as convert_time

def print_speed_options():
    print('sym  |use key')
    for key in DICTIONARIES.SPEED_KEY_TO_SYMBOL.keys():
        print('{:6s}{:6s}'.format(DICTIONARIES.SPEED_KEY_TO_SYMBOL[key], key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.SPEED_DECOMPOSITION[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.SPEED_DECOMPOSITION[ending]
    except KeyError:
        raise KeyError(ending)
        
    ret = value
    ret = convert_length(ret,
                         DICTIONARIES.SPEED_DECOMPOSITION[starting]["length"],
                         DICTIONARIES.SPEED_DECOMPOSITION[ending]["length"])
    # For conversions of units in the denominator, reverse starting and ending
    #     keys. Perhaps an update of this is to name it numerator/denominator
    #     instead of starting/ending.
    ret = convert_time(ret,
                       DICTIONARIES.SPEED_DECOMPOSITION[ending]["time"],
                       DICTIONARIES.SPEED_DECOMPOSITION[starting]["time"])
    return ret