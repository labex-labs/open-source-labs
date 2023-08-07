# Exercise 7.8: Simplifying Function Calls

In the above example, users might find calls such as `typedproperty('shares', int)` a bit verbose to type--especially if they're repeated a lot. Add the following definitions to the `typedproperty.py` file:

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

Now, rewrite the `Stock` class to use these functions instead:

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, that's a bit better. The main takeaway here is that closures and `lambda` can often be used to simplify code and eliminate annoying repetition. This is often good.
