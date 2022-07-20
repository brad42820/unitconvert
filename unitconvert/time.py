from .constants import CONSTANTS
from .dictionaries import DICTIONARIES

def print_time_options():
    print('sym|name        |use key')
    for key in DICTIONARIES.TIMES.keys():
        print('{:4s}{:13s}{:4s}'.format(key, DICTIONARIES.TIME_NAMES[key], key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.TIMES[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.TIMES[ending]
    except KeyError:
        raise KeyError(ending)
    return value*DICTIONARIES.TIMES[starting]/DICTIONARIES.TIMES[ending]