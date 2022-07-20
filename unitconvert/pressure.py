from .constants import CONSTANTS
from .dictionaries import DICTIONARIES
from .volume import convert as convert_volume
from .energy import convert as convert_energy

def print_pressure_options():
    print('symbol       |other name|use key')
    for key in DICTIONARIES.PRESSURE_KEY_TO_SYMBOL.keys():
        print('{:14s}{:11s}{:10s}'.format(key, DICTIONARIES.PRESSURE_KEY_TO_SYMBOL[key], key))

def convert(value, starting, ending):
    try:
        DICTIONARIES.PRESSURE_DECOMPOSITION[starting]
    except KeyError:
        raise KeyError(starting)
    try:
        DICTIONARIES.PRESSURE_DECOMPOSITION[ending]
    except KeyError:
        raise KeyError(ending)
        
    ret = value
    
    if starting == "atm":
        ret = ret*CONSTANTS.atm
        starting = "J/m^3"
    if ending == "atm":
        ret = ret/CONSTANTS.atm
        ending = "J/m^3"
        
    ret = convert_energy(ret,
                         DICTIONARIES.PRESSURE_DECOMPOSITION[starting]["energy"],
                         DICTIONARIES.PRESSURE_DECOMPOSITION[ending]["energy"])
    # For conversions of units in the denominator, reverse starting and ending
    #     keys. Perhaps an update of this is to name it numerator/denominator
    #     instead of starting/ending.
    ret = convert_volume(ret,
                       DICTIONARIES.PRESSURE_DECOMPOSITION[ending]["volume"],
                       DICTIONARIES.PRESSURE_DECOMPOSITION[starting]["volume"])
    return ret