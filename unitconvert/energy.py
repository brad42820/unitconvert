from .constants import CONSTANTS
from .dictionaries import DICTIONARIES

def print_energy_options():
    print('symbol   |use key')
    for key in DICTIONARIES.ENERGIES.keys():
        print('{:10s}{:4s}'.format(DICTIONARIES.ENERGY_KEY_TO_SYMBOL[key],
                                        key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.ENERGIES[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.ENERGIES[ending]
    except KeyError:
        raise KeyError(ending)
    return value*DICTIONARIES.ENERGIES[starting]/DICTIONARIES.ENERGIES[ending]