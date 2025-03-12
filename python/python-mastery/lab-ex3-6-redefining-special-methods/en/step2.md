# Making Objects Comparable with `__eq__`

In Python, the `==` operator calls the `__eq__` special method to compare objects. By default, it compares object identities (memory addresses), not their contents.

Let's see what happens when we create two identical `Stock` objects and try to compare them:

```bash
python3
```

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

Even though these objects have identical values, Python considers them different objects because they're stored at different memory locations.

We can fix this by implementing the `__eq__` method in our `Stock` class. This method gets called whenever the `==` operator is used on our objects.

Open the `stock.py` file again and add the `__eq__` method:

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

This method:

1. First checks if `other` is a `Stock` object using `isinstance`
2. If it is, compares the attributes of both objects
3. Returns `True` only if both objects are `Stock` instances with identical attributes

Your complete `Stock` class should now look like this:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

Now let's test our improved class:

```bash
python3
```

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

Great! Our objects can now be properly compared based on their content rather than their memory addresses.

The `isinstance` check is important because it ensures that we're only comparing `Stock` objects. Without it, comparing a `Stock` object with something else might raise errors.

Exit the Python interpreter when you're done:

```python
>>> exit()
```
