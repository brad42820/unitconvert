from .constants import CONSTANTS
from .dictionaries import DICTIONARIES

def print_mass_options():
    print('symbol |name               |use key')
    for key in DICTIONARIES.MASSES.keys():
        print('{:8s}{:20s}{:4s}'.format(DICTIONARIES.MASS_KEY_TO_SYMBOL[key],
                                        DICTIONARIES.MASS_NAMES[key], key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.MASSES[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.MASSES[ending]
    except KeyError:
        raise KeyError(ending)
    return value*DICTIONARIES.MASSES[starting]/DICTIONARIES.MASSES[ending]