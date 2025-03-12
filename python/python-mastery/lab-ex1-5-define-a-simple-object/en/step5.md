# Enhancing the Stock Class

In Python, classes are a powerful way to organize data and behavior. They allow us to group related data and functions together. In this section, we'll enhance our `Stock` class by adding a method that displays formatted stock information. This is a great example of how we can encapsulate both data and behavior in our classes. Encapsulation means bundling data with the methods that operate on that data, which helps in keeping our code organized and easier to manage.

1. First, you need to open the `stock.py` file in the WebIDE editor. The `stock.py` file is where we've been working on our `Stock` class. Opening it in the editor allows us to make changes to the class definition.

2. Now, we'll modify the `Stock` class to add a new `display()` method. This method will be responsible for printing out the stock information in a nicely formatted way. Here's how you can do it:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def display(self):
        print(f"Stock: {self.name}, Shares: {self.shares}, Price: ${self.price:.2f}, Total Cost: ${self.cost():.2f}")
```

In the `__init__` method, we initialize the stock's name, the number of shares, and the price. The `cost` method calculates the total cost of the stock by multiplying the number of shares by the price. The new `display` method uses an f-string to format and print the stock information, including the name, number of shares, price, and total cost.

3. After making these changes, you need to save the file. You can do this by pressing `Ctrl+S` on your keyboard or by clicking the Save icon in the editor. Saving the file ensures that your changes are preserved and can be used later.

4. Next, we'll start a new Python interactive session. An interactive session allows us to test our code immediately. To start the session, run the following command in the terminal:

```bash
python3 -i stock.py
```

The `-i` option tells Python to start an interactive session after executing the `stock.py` file. This way, we can use the `Stock` class and its methods right away.

5. Now, let's create a stock object and use the new `display()` method. We'll create an object representing Apple stock and then call the `display` method to see the formatted information. Here's the code:

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

When you run this code in the interactive session, you'll see the following output:

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

This output shows that the `display` method is working correctly and is formatting the stock information as expected.

6. Finally, let's create a list of stocks and display them all. This will show how we can use the `display` method with multiple stock objects. Here's the code:

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

When you run this code, you'll get the following output:

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

By adding the `display()` method to our class, we have encapsulated the formatting logic within the class itself. This makes our code more organized and easier to maintain. If we need to change the way the stock information is displayed, we only need to modify the `display` method in one place, rather than making changes throughout our code.
