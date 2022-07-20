from .constants import CONSTANTS
from .dictionaries import DICTIONARIES
from .length import convert as convert_length
from .energy import convert as convert_energy

def print_force_options():
    print('symbol      |other name|use key')
    for key in DICTIONARIES.FORCE_KEY_TO_SYMBOL.keys():
        print('{:13s}{:11s}{:10s}'.format(key, DICTIONARIES.FORCE_KEY_TO_SYMBOL[key], key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.FORCE_DECOMPOSITION[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.FORCE_DECOMPOSITION[ending]
    except KeyError:
        raise KeyError(ending)
        
    ret = value
    ret = convert_energy(ret,
                         DICTIONARIES.FORCE_DECOMPOSITION[starting]["energy"],
                         DICTIONARIES.FORCE_DECOMPOSITION[ending]["energy"])
    # For conversions of units in the denominator, reverse starting and ending
    #     keys. Perhaps an update of this is to name it numerator/denominator
    #     instead of starting/ending.
    ret = convert_length(ret,
                       DICTIONARIES.FORCE_DECOMPOSITION[ending]["length"],
                       DICTIONARIES.FORCE_DECOMPOSITION[starting]["length"])
    return ret