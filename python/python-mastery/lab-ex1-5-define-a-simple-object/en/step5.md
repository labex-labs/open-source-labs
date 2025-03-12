# Enhancing the Stock Class

Let's improve our `Stock` class by adding a method that displays formatted stock information. This demonstrates how we can encapsulate both data and behavior in our classes.

1. Open the `stock.py` file in the WebIDE editor.

2. Modify the `Stock` class to add a new `display()` method:

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

3. Save the file with `Ctrl+S` or by clicking the Save icon.

4. Start a new Python interactive session:

```bash
python3 -i stock.py
```

5. Create a stock object and use the new `display()` method:

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

Output:

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

6. Create a list of stocks and display them all:

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

Output:

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

By adding the `display()` method to our class, we have encapsulated the formatting logic within the class itself. This makes our code more organized and easier to maintain.
