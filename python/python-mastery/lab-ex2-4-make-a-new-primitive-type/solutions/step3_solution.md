# Step 3 Solution

Write the following program to `muint.py`:

```python
# mint.py

class MutInt:
    __slots__ = ["value"]

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"MutInt({self.value!r})"

    def __format__(self, fmt):
        return format(self.value, fmt)

    # Implement the "+" operator. Forward operands (MutInt + other)
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    # Support for reversed operands (other + MutInt)
    __radd__ = __add__

    # Support for in-place update (MutInt += other)
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Then, run this program in your terminal with the following command:

```bash
python3 -i mutint.py
```

Finally, run the code required in `step 3` in the `Python Shell`.
