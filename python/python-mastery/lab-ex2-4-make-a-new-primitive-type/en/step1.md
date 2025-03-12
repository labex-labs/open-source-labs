# Creating a Basic MutInt Class

Let's start by creating a basic class for our Mutable Integer type. In programming, a class is like a blueprint for creating objects. In this step, we'll create the foundation of our new primitive type. A primitive type is a basic data type provided by a programming language, and here we're going to build our own custom one.

1. Open the WebIDE and navigate to the `/home/labex/project` directory. The WebIDE is an integrated development environment where you can write, edit, and run your code. Navigating to this directory ensures that all your files are organized in one place and can interact with each other properly.

2. Open the `mutint.py` file that was created for you in the setup step. This file will be the home for our `MutInt` class definition.

3. Add the following code to define a basic `MutInt` class:

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value
```

The `__slots__` attribute is used to define the attributes that this class can have. Attributes are like variables that belong to an object of the class. By using `__slots__`, we tell Python to use a more memory - efficient way to store attributes. In this case, our `MutInt` class will only have a single attribute called `value`. This means that each object of the `MutInt` class will only be able to hold one piece of data, which is the integer value.

The `__init__` method is the constructor for our class. A constructor is a special method that gets called when an object of the class is created. It takes a value parameter and stores it in the `value` attribute of the instance. An instance is an individual object created from the class blueprint.

Let's test our class by creating a Python script to use it:

4. Create a new file called `test_mutint.py` in the same directory:

```python
# test_mutint.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)
print(f"Created MutInt with value: {a.value}")

# Modify the value (demonstrating mutability)
a.value = 42
print(f"Modified value to: {a.value}")

# Try adding (this will fail)
try:
    result = a + 10
    print(f"Result of a + 10: {result}")
except TypeError as e:
    print(f"Error when adding: {e}")
```

In this test script, we first import the `MutInt` class from the `mutint.py` file. Then we create an object of the `MutInt` class with an initial value of 3. We print the initial value, then modify it to 42 and print the new value. Finally, we try to add 10 to the `MutInt` object, which will result in an error because our class doesn't support the addition operation yet.

5. Run the test script by executing the following command in the terminal:

```bash
python3 /home/labex/project/test_mutint.py
```

The terminal is a command - line interface where you can run various commands to interact with your system and your code. Running this command will execute the `test_mutint.py` script.

You should see output similar to this:

```
Created MutInt with value: 3
Modified value to: 42
Error when adding: unsupported operand type(s) for +: 'MutInt' and 'int'
```

Our `MutInt` class successfully stores and updates a value. However, it has several limitations:

- It doesn't display nicely when printed
- It doesn't support mathematical operations like addition
- It doesn't support comparisons
- It doesn't support type conversions

In the next steps, we'll address these limitations one by one to make our `MutInt` class behave more like a true primitive type.
