# Preparation

Start this lab, by going back to a simple version of the `Stock` class you created.
At the interactive prompt, define a
new class called `SimpleStock` that looks like this:

```python
>>> class SimpleStock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def cost(self):
            return self.shares * self.price

>>>
```

Once you have defined this class, create a few instances.

```python
>>> goog = SimpleStock('GOOG',100,490.10)
>>> ibm  = SimpleStock('IBM',50, 91.23)
>>>
```
