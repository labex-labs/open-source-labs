# Step 2 Solution

# structure.py
...


class Structure(metaclass=StructureMeta):
    ...

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)

    ...
