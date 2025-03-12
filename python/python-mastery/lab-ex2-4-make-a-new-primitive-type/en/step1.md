# Creating a Basic MutInt Class

Let's start by creating a basic class for our Mutable Integer type. In this step, we'll create the foundation of our new primitive type.

1. Open the WebIDE and navigate to the `/home/labex/project` directory.

2. Open the `mutint.py` file that was created for you in the setup step.

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

The `__slots__` attribute is used to define the attributes that this class can have. By using `__slots__`, we tell Python to use a more memory-efficient way to store attributes. In this case, our `MutInt` class will only have a single attribute called `value`.

The `__init__` method is the constructor for our class. It takes a value parameter and stores it in the `value` attribute of the instance.

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

5. Run the test script by executing the following command in the terminal:

```bash
python3 /home/labex/project/test_mutint.py
```

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
