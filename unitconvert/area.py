from .constants import CONSTANTS
from .dictionaries import DICTIONARIES
from .length import convert as convert_length

def print_area_options():
    print('sym  |name        |use key')
    for key in DICTIONARIES.AREA_NAMES.keys():
        print('{:6s}{:13s}{:6s}'.format(DICTIONARIES.AREA_KEY_TO_SYMBOL[key],
                                        DICTIONARIES.AREA_NAMES[key],
                                        key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.AREA_DECOMPOSITION[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.AREA_DECOMPOSITION[ending]
    except KeyError:
        raise KeyError(ending)
        
    ret = value
    for keyS,keyE in zip(DICTIONARIES.AREA_DECOMPOSITION[starting],
                     DICTIONARIES.AREA_DECOMPOSITION[ending]):
        ret = convert_length(ret, keyS, keyE)
    return ret