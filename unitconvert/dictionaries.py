from .constants import CONSTANTS

def dictionaries(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Dictionaries(object):
    @dictionaries
    def LENGTHS():
        return {"Mm":1e6, "km":1e3, "m":1, "cm":1e-2, "mm":1e-3, "um":1e-6,
                "nm":1e-9, "A":1e-10}
    @dictionaries
    def LENGTH_NAMES():
        return {"Mm":"megameters", "km":"kilometers", "m":"meters",
                "cm":"centimeters", "mm":"millimeters", "um":"micrometers",
                "nm":"nanometers", "A":"Angstroms"}
    @dictionaries
    def AREA_NAMES():
        return {"Mm^2":"megameters\u00b2",
                "km^2":"kilometers\u00b2",
                "m^2":"meters\u00b2",
                "cm^2":"centimeters\u00b2",
                "mm^2":"millimeters\u00b2",
                "um^2":"micrometers\u00b2",
                "nm^2":"nanometers\u00b2",
                "A^2":"Angstroms\u00b2"}
    @dictionaries
    def AREA_KEY_TO_SYMBOL():
        return {"Mm^2":"Mm\u00b2",
                "km^2":"km\u00b2",
                "m^2":"m\u00b2",
                "cm^2":"cm\u00b2",
                "mm^2":"mm\u00b2",
                "um^2":"um\u00b2",
                "nm^2":"nm\u00b2",
                "A^2":"A\u00b2"}
    @dictionaries
    def AREA_DECOMPOSITION():
        return {"Mm^2":["Mm","Mm"],
                "km^2":["km","km"],
                "m^2":["m","m"],
                "cm^2":["cm","cm"],
                "mm^2":["mm","mm"],
                "um^2":["um","um"],
                "nm^2":["nm","nm"],
                "A^2":["A","A"]}
    @dictionaries
    def VOLUME_NAMES():
        return {"Mm^3":"megameters\u00b3",
                "km^3":"kilometers\u00b3",
                "m^3":"meters\u00b3",
                "cm^3":"centimeters\u00b3",
                "mm^3":"millimeters\u00b3",
                "um^3":"micrometers\u00b3",
                "nm^3":"nanometers\u00b3",
                "A^3":"Angstroms\u00b3"}
    @dictionaries
    def VOLUME_KEY_TO_SYMBOL():
        return {"Mm^3":"Mm\u00b3",
                "km^3":"km\u00b3",
                "m^3":"m\u00b3",
                "cm^3":"cm\u00b3",
                "mm^3":"mm\u00b3",
                "um^3":"um\u00b3",
                "nm^3":"nm\u00b3",
                "A^3":"A\u00b3"}
    @dictionaries
    def VOLUME_DECOMPOSITION():
        return {"Mm^3":["Mm","Mm","Mm"],
                "km^3":["km","km","km"],
                "m^3":["m","m","m"],
                "cm^3":["cm","cm","cm"],
                "mm^3":["mm","mm","mm"],
                "um^3":["um","um","um"],
                "nm^3":["nm","nm","nm"],
                "A^3":["A","A","A"]}
    @dictionaries
    def TIMES():
        return {"Ms":1e6, "ks":1e3, "s":1, "cs":1e-2, "ms":1e-3, "us":1e-6,
                "ns":1e-9, "ps":1e-12}
    @dictionaries
    def TIME_NAMES():
        return {"Ms":"megaseconds", "ks":"kiloseconds", "s":"seconds",
                "cs":"centiseconds", "ms":"milliseconds", "us":"microseconds",
                "ns":"nanoseconds", "ps":"picoseconds"}
    @dictionaries
    def SPEED_KEY_TO_SYMBOL():
        return {"km/s":"km/s",
                "m/s":"m/s",
                "cm/s":"cm/s",
                "mm/s":"mm/s",
                "mm/ms":"mm/ms",
                "um/ms":"\u00b5m/ms",
                "um/us":"\u00b5m/\u00b5s",
                "nm/ns":"nm/ns",
                "nm/ps":"nm/ps"}
    @dictionaries
    def SPEED_DECOMPOSITION():
        return {"km/s":{"length":"km", "time":"s"},
                "m/s":{"length":"m", "time":"s"},
                "cm/s":{"length":"cm", "time":"s"},
                "mm/s":{"length":"mm", "time":"s"},
                "mm/ms":{"length":"mm", "time":"ms"},
                "um/ms":{"length":"um", "time":"ms"},
                "um/us":{"length":"um", "time":"us"},
                "nm/ns":{"length":"nm", "time":"ns"},
                "nm/ps":{"length":"nm", "time":"ps"}}
    @dictionaries
    def ACCELERATION_KEY_TO_SYMBOL():
        return {"km/s^2":"km/s\u00b2",
                "m/s^2":"m/s\u00b2",
                "cm/s^2":"cm/s\u00b2",
                "mm/s^2":"mm/s\u00b2",
                "mm/ms^2":"mm/ms\u00b2",
                "um/ms^2":"\u00b5m/ms\u00b2",
                "um/us^2":"\u00b5m/\u00b5s\u00b2",
                "nm/ns^2":"nm/ns\u00b2",
                "nm/ps^2":"nm/ps\u00b2"}
    @dictionaries
    def ACCELERATION_DECOMPOSITION():
        return {"km/s^2":{"length":"km", "time":["s","s"]},
                "m/s^2":{"length":"m", "time":["s","s"]},
                "cm/s^2":{"length":"cm", "time":["s","s"]},
                "mm/s^2":{"length":"mm", "time":["s","s"]},
                "mm/ms^2":{"length":"mm", "time":["ms","ms"]},
                "um/ms^2":{"length":"um", "time":["ms","ms"]},
                "um/us^2":{"length":"um", "time":["us","us"]},
                "nm/ns^2":{"length":"nm", "time":["ns","ns"]},
                "nm/ps^2":{"length":"nm", "time":["ps","ps"]}}
    @dictionaries
    def MASSES():
        return {"kg":1e3,"g":1,"mg":1e-3,"ug":1e-6,
                "ng":1e-9,"pg":1e-12,"u":1.6605391e-24}
    @dictionaries
    def MASS_KEY_TO_SYMBOL():
        return {"kg":"kg","g":"g","mg":"mg","ug":"\u00b5g",
                "ng":"ng","pg":"pg","u":"amu"}
    @dictionaries
    def MASS_NAMES():
        return {"kg":"kilograms", "g":"grams", "mg":"milligrams",
                "ug": "micrograms", "pg": "picograms",
                "ng":"nanograms", "u":"atomic mass units"}
    @dictionaries
    def ENERGIES():
        return {"kJ":1e3,"J":1,"kcal":4184,
                "kJ/mol":1e3/CONSTANTS.Avogadro,
                "kcal/mol":4184/CONSTANTS.Avogadro}
    @dictionaries
    def ENERGY_KEY_TO_SYMBOL():
        return {"kJ":"kJ","J":"J","kcal":"kcal",
                "kJ/mol":"kJ/mol","kcal/mol":"kcal/mol"}
    @dictionaries
    def FORCE_KEY_TO_SYMBOL():
        return {"J/m":"N",
                "kJ/m":"kN",
                "J/mm":"kN",
                "kcal/m":"",
                "kJ/mol-m":"kN/mol",
                "kJ/mol-nm":"TN/mol",
                "kcal/mol-nm":"",
                "kcal/mol-A":""}
    @dictionaries
    def FORCE_DECOMPOSITION():
        return {"J/m":{"length":"m", "energy":"J"},
                "kJ/m":{"length":"m", "energy":"kJ"},
                "J/mm":{"length":"mm", "energy":"J"},
                "kcal/m":{"length":"m", "energy":"kcal"},
                "kJ/mol-m":{"length":"m", "energy":"kJ/mol"},
                "kJ/mol-nm":{"length":"nm", "energy":"kJ/mol"},
                "kcal/mol-nm":{"length":"nm", "energy":"kcal/mol"},
                "kcal/mol-A":{"length":"A", "energy":"kcal/mol"}}
    @dictionaries
    def PRESSURE_KEY_TO_SYMBOL():
        return {"atm":"",
                "J/m^3":"Pa",
                "J/cm^3":"MPa",
                "J/mm^3":"GPa",
                "kJ/m^3":"kPa",
                "kJ/cm^3":"GPa",
                "kJ/mm^3":"TPa",
                "kJ/mol-m^3":"kPa/mol",
                "kJ/mol-nm^3":"",
                "kcal/m^3":"",
                "kcal/mol-nm^3":"",
                "kcal/mol-A^3":""}
    @dictionaries
    def PRESSURE_DECOMPOSITION():
        return {"atm":{"volume":"m^3", "energy":"J"},
                # A special line of code converts between atm and Pa.
                "J/m^3":{"volume":"m^3", "energy":"J"},
                "J/cm^3":{"volume":"cm^3", "energy":"J"},
                "J/mm^3":{"volume":"mm^3", "energy":"J"},
                "kJ/m^3":{"volume":"m^3", "energy":"kJ"},
                "kJ/cm^3":{"volume":"cm^3", "energy":"kJ"},
                "kJ/mm^3":{"volume":"mm^3", "energy":"kJ"},
                "kJ/mol-m^3":{"volume":"m^3", "energy":"kJ/mol"},
                "kJ/mol-nm^3":{"volume":"nm^3", "energy":"kJ/mol"},
                "kcal/m^3":{"volume":"m^3", "energy":"kcal"},
                "kcal/mol-nm^3":{"volume":"nm^3", "energy":"kcal/mol"},
                "kcal/mol-A^3":{"volume":"A^3", "energy":"kcal/mol"}}
    

DICTIONARIES = _Dictionaries()