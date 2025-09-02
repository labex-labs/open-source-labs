# Creating a Class Decorator for Validation

In the previous step, our implementation worked, but there was a redundancy. We had to specify both the `_fields` tuple and the descriptor attributes. This is not very efficient, and we can improve it. In Python, class decorators are a powerful tool that can help us simplify this process. A class decorator is a function that takes a class as an argument, modifies it in some way, and then returns the modified class. By using a class decorator, we can automatically extract field information from the descriptors, which will make our code cleaner and more maintainable.

Let's create a class decorator to simplify our code. Here are the steps you need to follow:

1. First, open the `structure.py` file in your editor.

2. Next, add the following code at the top of the `structure.py` file, right after any import statements. This code defines our class decorator:

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

Let's break down what this decorator does:

- It first creates an empty list called `validators`. Then, it iterates over all the attributes of the class using `vars(cls).items()`. If an attribute is an instance of the `Validator` class, it adds that attribute to the `validators` list.
- After that, it sets the `_fields` attribute of the class. It creates a list of names from the validators in the `validators` list and assigns it to `cls._fields`.
- Finally, it calls the `create_init()` method of the class to generate the `__init__` method, and then returns the modified class.

3. Once you've added the code, save the `structure.py` file. Saving the file ensures that your changes are preserved.

4. Now, we need to modify our `stock.py` file to use this new decorator. Open the `stock.py` file in your editor.

5. Update the `stock.py` file to use the `validate_attributes` decorator. Replace the existing code with the following:

```python
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
```

Notice the changes we've made:

- We added the `@validate_attributes` decorator right above the `Stock` class definition. This tells Python to apply the `validate_attributes` decorator to the `Stock` class.
- We removed the explicit `_fields` declaration because the decorator will handle it automatically.
- We also removed the call to `Stock.create_init()` because the decorator takes care of creating the `__init__` method.

As a result, the class is now simpler and cleaner. The decorator takes care of all the details that we used to handle manually.

6. After making these changes, we need to verify that everything still works as expected. Run the tests again using the following commands:

```bash
cd ~/project
python3 teststock.py
```

If everything is working correctly, you should see the following output:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

This output indicates that all the tests have passed successfully.

Let's also test our `Stock` class interactively. Run the following command in the terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

You should see the following output:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Great! You've successfully implemented a class decorator that simplifies our code by automatically handling field declarations and initialization. This makes our code more efficient and easier to maintain.
