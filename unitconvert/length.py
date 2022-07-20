from .constants import CONSTANTS
from .dictionaries import DICTIONARIES

def print_length_options():
    print('sym|name        |use key')
    for key in DICTIONARIES.LENGTHS.keys():
        print('{:4s}{:13s}{:4s}'.format(key, DICTIONARIES.LENGTH_NAMES[key], key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.LENGTHS[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.LENGTHS[ending]
    except KeyError:
        raise KeyError(ending)
    return value*DICTIONARIES.LENGTHS[starting]/DICTIONARIES.LENGTHS[ending]