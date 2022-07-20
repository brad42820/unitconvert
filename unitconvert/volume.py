from .constants import CONSTANTS
from .dictionaries import DICTIONARIES
from .length import convert as convert_length

def print_volume_options():
    print('sym  |name        |use key')
    for key in DICTIONARIES.VOLUME_NAMES.keys():
        print('{:6s}{:13s}{:6s}'.format(DICTIONARIES.VOLUME_KEY_TO_SYMBOL[key],
                                        DICTIONARIES.VOLUME_NAMES[key],
                                        key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.VOLUME_DECOMPOSITION[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.VOLUME_DECOMPOSITION[ending]
    except KeyError:
        raise KeyError(ending)
        
    ret = value
    for keyS,keyE in zip(DICTIONARIES.VOLUME_DECOMPOSITION[starting],
                     DICTIONARIES.VOLUME_DECOMPOSITION[ending]):
        ret = convert_length(ret, keyS, keyE)
    return ret