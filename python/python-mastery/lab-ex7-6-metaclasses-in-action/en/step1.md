# Understanding the Problem

Before we start exploring metaclasses, it's important to understand the problem we aim to solve. In programming, we often need to create structures with specific types for their attributes. In our previous work, we developed a system for type - checked structures. This system allows us to define classes where each attribute has a specific type, and the values assigned to these attributes are validated according to that type.

Here is an example of how we used this system to create a `Stock` class:

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

In this code, we first import the validator types (`String`, `PositiveInteger`, `PositiveFloat`) from the `validate` module and the `Structure` class from the `structure` module. Then we define the `Stock` class, which inherits from `Structure`. Inside the `Stock` class, we define attributes with specific validator types. For example, the `name` attribute must be a string, `shares` must be a positive integer, and `price` must be a positive float.

However, there is an issue with this approach. We need to import all the validator types at the top of our file. As we add more and more validator types in a real - world scenario, these imports can become very long and difficult to manage. This might lead us to use `from validate import *`, which is generally considered a bad practice because it can cause naming conflicts and make the code less readable.

To understand our starting point, let's take a look at the `Structure` class. You need to open the `structure.py` file in the editor and examine its contents. This will help you see how the basic structure handling is implemented before we add metaclass functionality.

```bash
code structure.py
```

When you open the file, you'll see a basic implementation of the `Structure` class. This class is responsible for handling attribute initialization, but it doesn't have any metaclass functionality yet.

Next, let's examine the validator classes. These classes are defined in the `validate.py` file. They already have descriptor functionality, which means they can control how attributes are accessed and set. But we'll need to enhance them to solve the import problem we discussed earlier.

```bash
code validate.py
```

By looking at these validator classes, you'll get a better understanding of how the validation process works and what changes we need to make to improve our code.
