# Creating the Stock Class

Now, let's create our `Stock` class to represent stock information. We will define attributes for the stock name, number of shares, and price per share.

1. In the WebIDE, navigate to the `/home/labex/project` directory if you're not already there.

2. Create a new file named `stock.py` in the editor.

3. Add the following code to define the `Stock` class:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

4. Save the file by pressing `Ctrl+S` or clicking the Save icon.

Let's examine the code:

- We defined a class named `Stock`.
- The `__init__` method takes three parameters: `name`, `shares`, and `price`.
- Inside `__init__`, we store these parameters as instance attributes using `self`.
- We added a `cost()` method that calculates the total cost by multiplying shares by price.

When we create a `Stock` object, the `__init__` method will run automatically, setting up the initial state of our object with the values we provide.
