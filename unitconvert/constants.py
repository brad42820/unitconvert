def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Constant(object):
    @constant
    def Avogadro():
        return 6.0221408e23
    @constant
    def kB():
        return 1.380649e-23
    @constant
    def atm():
        return 101325

CONSTANTS = _Constant()