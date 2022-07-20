from .constants import CONSTANTS
from .dictionaries import DICTIONARIES
from .length import convert as convert_length
from .time import convert as convert_time

def print_acceleration_options():
    print('symbol |use key')
    for key in DICTIONARIES.ACCELERATION_KEY_TO_SYMBOL.keys():
        print('{:8s}{:6s}'.format(DICTIONARIES.ACCELERATION_KEY_TO_SYMBOL[key], key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.ACCELERATION_DECOMPOSITION[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.ACCELERATION_DECOMPOSITION[ending]
    except KeyError:
        raise KeyError(ending)
        
    ret = value
    ret = convert_length(ret,
                         DICTIONARIES.ACCELERATION_DECOMPOSITION[starting]["length"],
                         DICTIONARIES.ACCELERATION_DECOMPOSITION[ending]["length"])
    
    for keyS,keyE in zip(DICTIONARIES.ACCELERATION_DECOMPOSITION[starting]["time"],
                         DICTIONARIES.ACCELERATION_DECOMPOSITION[ending]["time"]):
        # For conversions of units in the denominator, reverse starting and ending
        #     keys. Perhaps an update of this is to name it numerator/denominator
        #     instead of starting/ending.
        ret = convert_time(ret, keyE, keyS)
    return ret