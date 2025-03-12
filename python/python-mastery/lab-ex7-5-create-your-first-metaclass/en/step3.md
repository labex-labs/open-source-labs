# Using Your Metaclass

Now let's create a class that uses our metaclass via inheritance. We'll see how the metaclass is invoked when the class is defined.

1. Open `mymeta.py` and add the following code at the end of the file:

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

2. Save the file by pressing Ctrl+S.

3. Now let's run the file to see what happens. Open a terminal in the WebIDE and run:

```bash
cd /home/labex/project
python3 mymeta.py
```

You should see output similar to this:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

This output shows that our metaclass is being invoked when both `myobject` and `Stock` classes are created. Notice how:

- For `Stock`, the base classes include `myobject`
- The attributes list includes all the methods we defined

4. Let's interact with our `Stock` class. Create a new file named `test_stock.py` with the following content:

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

5. Run this file to test our `Stock` class:

```bash
python3 test_stock.py
```

You should see output like:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

Notice that our metaclass information is printed first, followed by the output from our test script.
