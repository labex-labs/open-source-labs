# Step 2 Solution

# structure.py


class Structure:
    _fields = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected %d arguments" % len(self._fields))
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)
