# Step 2 Solution

# structure.py

from validate import Validator


class Structure:
    _fields = ()
    _types = ()

    def __setattr__(self, name, value):
        if name.startswith("_") or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError("No attribute %s" % name)

    def __repr__(self):
        return "%s(%s)" % (
            type(self).__name__,
            ", ".join(repr(getattr(self, name)) for name in self._fields),
        )

    @classmethod
    def create_init(cls):
        """
        Create an __init__ method from _fields
        """
        args = ",".join(cls._fields)
        code = f"def __init__(self, {args}):\n"
        for name in cls._fields:
            code += f"    self.{name} = {name}\n"
        locs = {}
        exec(code, locs)
        cls.__init__ = locs["__init__"]


def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]
    return cls


# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares