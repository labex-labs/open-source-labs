# Understanding the Problem

Before we dive into metaclasses, let's understand the problem we're trying to solve. In previous work, we created a system for type-checked structures that looks like this:

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

The issue here is that we need to import all validator types (`String`, `PositiveInteger`, `PositiveFloat`) at the top of our file. As more validator types are added, these imports can become unwieldy and could lead to the use of `from validate import *`, which is generally considered a poor practice.

Let's look at the `Structure` class to understand our starting point. Open the `structure.py` file in the editor and examine its contents:

```bash
code structure.py
```

You should see a basic implementation of the `Structure` class that handles attribute initialization but doesn't yet have any metaclass functionality.

Now let's examine the validator classes:

```bash
code validate.py
```

These validator classes already have descriptor functionality in place, but we'll need to enhance them to solve our import problem.
