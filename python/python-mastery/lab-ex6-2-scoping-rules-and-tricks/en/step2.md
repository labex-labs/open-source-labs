# Using locals() to Access Function Arguments

Python provides a built-in function called `locals()` that returns a dictionary containing all local variables in the current scope. This can be very useful for inspecting function arguments.

Let's create a simple experiment in the Python interpreter to see how this works:

```bash
cd ~/project
python3
```

In the Python interactive shell, define a `Stock` class with a special `__init__` method that prints all local variables:

```python
class Stock:
    def __init__(self, name, shares, price):
        print(locals())
```

Now, create an instance of this class:

```python
s = Stock('GOOG', 100, 490.1)
```

You should see output similar to:

```
{'self': <__main__.Stock object at 0x...>, 'name': 'GOOG', 'shares': 100, 'price': 490.1}
```

This shows that `locals()` gives us a dictionary containing all the local variables in the `__init__` method, including the parameter values and the `self` reference.

We can use this to automatically initialize object attributes. Let's define a helper function and modify our `Stock` class:

```python
def _init(locs):
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init(locals())
```

Now, test this implementation with both positional and keyword arguments:

```python
# Test with positional arguments
s1 = Stock('GOOG', 100, 490.1)
print(s1.name, s1.shares, s1.price)

# Test with keyword arguments
s2 = Stock(name='AAPL', shares=50, price=125.3)
print(s2.name, s2.shares, s2.price)
```

Both approaches should work now! The `_init` function takes the dictionary of local variables, removes the `self` reference, and then sets each of the remaining variables as attributes on the object.

This is a powerful technique that allows us to handle both positional and keyword arguments seamlessly. It also preserves the parameter names in the function signature, making the `help()` output more useful.

When you're done experimenting, exit the Python interpreter:

```python
exit()
```
