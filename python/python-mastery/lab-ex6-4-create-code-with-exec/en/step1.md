# Understanding the Basics of exec()

In Python, the `exec()` function is a powerful tool that allows you to execute code that is created dynamically at runtime. This means you can generate code on the fly based on certain input or configuration, which is extremely useful in many programming scenarios.

Let's start by exploring the basic usage of the `exec()` function. To do this, we'll open a Python shell. Open your terminal and type `python3`. This command will start the interactive Python interpreter, where you can directly run Python code.

```bash
python3
```

Now, we're going to define a piece of Python code as a string and then use the `exec()` function to execute it. Here's how it works:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

In this example:

1. First, we defined a string named `code`. This string contains a Python for-loop. The loop is designed to iterate `n` times and print each iteration number.
2. Then, we defined a variable `n` and assigned it the value 10. This variable is used as the upper bound for the `range()` function in our loop.
3. After that, we called the `exec()` function with the `code` string as an argument. The `exec()` function takes the string and executes it as Python code.
4. Finally, the loop ran and printed the numbers from 0 to 9.

The real power of the `exec()` function becomes more obvious when we use it to create more complex code structures, such as functions or methods. Let's try a more advanced example where we'll dynamically create an `__init__()` method for a class.

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

In this more complex example:

1. We first defined a `Stock` class with a `_fields` attribute. This attribute is a tuple that contains the names of the class's attributes.
2. Then, we created a string that represents Python code for an `__init__` method. This method is used to initialize the object's attributes.
3. Next, we used the `exec()` function to execute the code string. We also passed an empty dictionary `locs` to `exec()`. The resulting function from the execution is stored in this dictionary.
4. After that, we assigned the function stored in the dictionary as the `__init__` method of our `Stock` class.
5. Finally, we created an instance of the `Stock` class and verified that the `__init__` method works correctly by accessing the object's attributes.

This example demonstrates how the `exec()` function can be used to dynamically create methods based on data that is available at runtime.
