# Step 3 Solution

# structure.py
...
        
class Structure(metaclass=StructureMeta):
    ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
    ...