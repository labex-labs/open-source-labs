# Adding a sell Method to the Stock Class

In this step, we're going to enhance the `Stock` class by adding a new method. A method is like a special function that belongs to a class and can work with the objects created from that class. We'll create a method named `sell(nshares)` which will help us simulate the action of selling shares of a stock. When you sell shares, the number of shares you own decreases, and this method will handle that reduction for us.

## What is a Method?

Let's first understand what a method is. A method is a function that is defined inside a class. It's designed to operate on instances (which are like individual copies) of that class. When a method is called on an object, it can access all the attributes (characteristics) of that object. It does this through the `self` parameter. The `self` parameter is a reference to the object on which the method is being called. So, when you use `self` inside a method, you're referring to the specific object that the method is acting on.

## Implementation Instructions

1. First, we need to open the `stock.py` file in the editor. To do this, we'll use the command line. Open your terminal and run the following command. This command changes the directory to the `project` folder where the `stock.py` file is located.

```bash
cd ~/project
```

2. Once you have the `stock.py` file open, you need to find a specific comment in the `Stock` class. Look for the comment `# TODO: Add sell(nshares) method here`. This comment is a placeholder that indicates where we should add our new `sell` method.

3. Now, it's time to add the `sell` method. This method will take a parameter called `nshares`, which represents the number of shares you want to sell. The main job of this method is to decrease the `shares` attribute of the `Stock` object by the number of shares you're selling.

Here's the code for the `sell` method that you need to add:

```python
def sell(self, nshares):
    self.shares -= nshares
```

In this code, `self.shares` refers to the `shares` attribute of the `Stock` object. The `-=` operator subtracts the value of `nshares` from the current value of `self.shares`.

4. After adding the `sell` method, you need to save the `stock.py` file. You can do this by pressing `Ctrl+S` on your keyboard or by selecting "File > Save" from the menu in your editor.

5. To make sure our `sell` method works correctly, we'll create a test script. Create a new Python file called `test_sell.py` and add the following code to it:

```python
# test_sell.py
from stock import Stock

# Create a stock object
s = Stock('GOOG', 100, 490.10)
print(f"Initial shares: {s.shares}")

# Sell 25 shares
s.sell(25)
print(f"Shares after selling: {s.shares}")
```

In this script, we first import the `Stock` class from the `stock.py` file. Then we create a `Stock` object named `s` with the stock symbol `GOOG`, 100 shares, and a price of 490.10. We print the initial number of shares. After that, we call the `sell` method on the `s` object to sell 25 shares. Finally, we print the number of shares after the sale.

6. Now, we'll run the test script to see if our `sell` method is working as expected. Open your terminal again and run the following command:

```bash
python3 test_sell.py
```

If everything is working correctly, you should see output similar to this:

```
Initial shares: 100
Shares after selling: 75
```

This output confirms that our `sell` method is working correctly. It has successfully reduced the number of shares by the amount we specified.
