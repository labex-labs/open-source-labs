# Understanding Python Modules

A Python module is simply a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. Modules allow you to logically organize your Python code, making it more reusable and maintainable.

Let's examine the files that have been prepared for this lab:

1. Open the `stock.py` file in the editor to view its contents:

```bash
cd ~/project
cat stock.py
```

This file defines a `Stock` class that represents a stock with attributes for name, shares, and price, along with a method to calculate its cost.

2. Now, examine the `pcost.py` file:

```bash
cat pcost.py
```

This file defines a function `portfolio_cost()` that reads a portfolio file and calculates the total cost of all stocks in the portfolio.

3. Look at the sample portfolio data:

```bash
cat portfolio.dat
```

This file contains stock data in a simple format: ticker symbol, number of shares, and price per share.

## Using the import Statement

Python's `import` statement allows you to use code from other modules in your current program. Let's practice using different import techniques:

1. Start the Python interpreter:

```bash
python3
```

2. Import the `pcost` module and observe its behavior:

```python
import pcost
```

You should see the output `44671.15`, which is the calculated cost of the portfolio from the `portfolio.dat` file. This happens because the code at the bottom of `pcost.py` runs automatically when the module is imported.

3. Try calling the function with a different portfolio file:

```python
pcost.portfolio_cost('portfolio2.dat')
```

The output should be `19908.75`, representing the total cost of stocks in the second portfolio file.

4. Now, import a specific class from the `stock` module:

```python
from stock import Stock
```

5. Create a Stock object and interact with it:

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
```

The output should be:

```
GOOG
49010.0
```

6. Exit the Python interpreter:

```python
exit()
```

This demonstrates two different ways to import Python code:

- `import module_name` - imports the entire module
- `from module_name import specific_item` - imports only a specific item from the module
