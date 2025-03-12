# Implementing Type-Checking with Descriptors

In this step, we're going to create a `Stock` class that uses descriptors for type checking. But first, let's understand what descriptors are. Descriptors are a really powerful feature in Python. They give you control over how attributes are accessed in classes.

Descriptors are objects that define how attributes are accessed on other objects. They do this by implementing special methods like `__get__`, `__set__`, and `__delete__`. These methods allow descriptors to manage how attributes are retrieved, set, and deleted. Descriptors are very useful for implementing validation, type checking, and computed properties. For example, you can use a descriptor to make sure that an attribute is always a positive number or a string of a certain format.

The `validate.py` file already has validator classes (`String`, `PositiveInteger`, `PositiveFloat`). We can use these classes to validate the attributes of our `Stock` class.

Now, let's create our `Stock` class with descriptors.

1. First, open the `stock.py` file in the editor. You can do this by running the following command in your terminal:

```bash
code ~/project/stock.py
```

This command uses the `code` editor to open the `stock.py` file located in the `~/project` directory.

2. Once the file is open, replace the placeholder content with the following code:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Create an __init__ method based on _fields
Stock.create_init()
```

Let's break down what this code does. The `_fields` tuple defines the attributes of the `Stock` class. These are the names of the attributes that our `Stock` objects will have.

The `name`, `shares`, and `price` attributes are defined as descriptor objects. The `String()` descriptor ensures that the `name` attribute is a string. The `PositiveInteger()` descriptor makes sure that the `shares` attribute is a positive integer. And the `PositiveFloat()` descriptor guarantees that the `price` attribute is a positive floating-point number.

The `cost` property is a computed property. It calculates the total cost of the stock based on the number of shares and the price per share.

The `sell` method is used to reduce the number of shares. When you call this method with a number of shares to sell, it subtracts that number from the `shares` attribute.

The `Stock.create_init()` line dynamically creates an `__init__` method for our class. This method allows us to create `Stock` objects by passing in the values for the `name`, `shares`, and `price` attributes.

3. After you've added the code, save the file. This will make sure that your changes are saved and can be used when you run the tests.

4. Now, let's run the tests to verify your implementation. First, change the directory to the `~/project` directory by running the following command:

```bash
cd ~/project
```

Then, run the tests using the following command:

```bash
python3 teststock.py
```

If your implementation is correct, you should see output similar to this:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

This output means that all the tests are passing. The descriptors are successfully validating the types of each attribute!

Let's try creating a `Stock` object in the Python interpreter. First, make sure you're in the `~/project` directory. Then, run the following command:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

You should see the following output:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

You've successfully implemented descriptors for type-checking! Now, let's improve this code further.
