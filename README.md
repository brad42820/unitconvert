# unitconvert
Convert between units for MD simulations.

## Installation
<pre>
pip install git+https://github.com/brad42820/unitconvert.git
</pre>

## Usage
Currently, the quantities that are implemented for conversion include:
- length
- area
- volume
- time
- speed
- acceleration
- energy
- mass
- force
- pressure

### Printing Unit Options
The units that are available for conversion can be listed using commands of the type:
<pre>
&#8921; unitconvert.pressure.print_pressure_options()
symbol       |other name|use key
atm                      atm       
J/m^3         Pa         J/m^3     
J/cm^3        MPa        J/cm^3    
J/mm^3        GPa        J/mm^3    
kJ/m^3        kPa        kJ/m^3    
kJ/cm^3       GPa        kJ/cm^3   
kJ/mm^3       TPa        kJ/mm^3   
kJ/mol-m^3    kPa/mol    kJ/mol-m^3
kJ/mol-nm^3              kJ/mol-nm^3
kcal/m^3                 kcal/m^3  
kcal/mol-nm^3            kcal/mol-nm^3
kcal/mol-A^3             kcal/mol-A^3
</pre>

You can replace pressure with the quantity of interest. The columns listed include **symbol:** the way in which you might write the unit by hand, **other name** or **name:** alternate ways to express the same unit, and **use key:** the text that you should enter in the *convert* method (see below).

### Constants
A few physical constants are available:  
*unitconvert.CONSTANTS.Avogadro* - Avogadro's number  
*unitconvert.CONSTANTS.atm* - the number of Pascals in an atmosphere  
*unitconvert.CONSTANTS.kB* - Boltzmann's constant  

### Unit Conversion
<pre>
&#8921; unitconvert.pressure.convert(value, starting, ending)
</pre>

**value** is the pressure in the starting units.  
**starting** and **ending** are the keys associated with the starting and ending units. See above for how to list the keys to use.
