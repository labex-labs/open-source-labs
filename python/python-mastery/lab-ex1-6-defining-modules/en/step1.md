# Understanding Python Modules

In Python, a module is like a container that holds Python definitions and statements. It's essentially a file, and the name of this file is the module name with the `.py` extension added at the end. Think of modules as toolboxes. They help you organize your Python code in a logical way, making it easier to reuse and maintain. Just like you'd keep different tools in separate boxes for better organization, you can group related Python code into different modules.

Let's take a look at the files that have been set up for this lab:

1. First, we'll open the `stock.py` file in the editor to see what's inside. To do this, we'll use the following commands. The `cd` command changes the directory to the `project` folder where our file is located, and the `cat` command displays the contents of the file.

```bash
cd ~/project
cat stock.py
```

This `stock.py` file defines a `Stock` class. A class is like a blueprint for creating objects. In this case, the `Stock` class represents a stock. It has attributes (which are like characteristics) for the stock's name, the number of shares, and the price. It also has a method (which is like a function associated with the class) to calculate the cost of the stock.

2. Next, let's examine the `pcost.py` file. We'll use the `cat` command again to view its contents.

```bash
cat pcost.py
```

This file defines a function called `portfolio_cost()`. A function is a block of code that performs a specific task. The `portfolio_cost()` function reads a portfolio file and calculates the total cost of all the stocks in that portfolio.

3. Now, let's look at the sample portfolio data. We'll use the `cat` command to view the contents of the `portfolio.dat` file.

```bash
cat portfolio.dat
```

This file contains stock data in a simple format. Each line has the ticker symbol of the stock, the number of shares, and the price per share.

## Using the import Statement

Python's `import` statement is a powerful tool that allows you to use code from other modules in your current program. It's like borrowing tools from other toolboxes. Let's practice using different ways to import code:

1. First, we need to start the Python interpreter. The Python interpreter is a program that executes Python code. We'll use the following command to start it.

```bash
python3
```

2. Now, let's import the `pcost` module and see what happens. When we use the `import` statement, Python looks for the `pcost.py` file and makes the code inside it available for us to use.

```python
import pcost
```

You should see the output `44671.15`. This is the calculated cost of the portfolio from the `portfolio.dat` file. When the `pcost` module is imported, the code at the bottom of the `pcost.py` file runs automatically.

3. Let's try calling the `portfolio_cost()` function with a different portfolio file. We'll use the `pcost.portfolio_cost()` syntax to call the function from the `pcost` module.

```python
pcost.portfolio_cost('portfolio2.dat')
```

The output should be `19908.75`, which represents the total cost of the stocks in the second portfolio file.

4. Now, let's import a specific class from the `stock` module. Instead of importing the whole module, we can just import the `Stock` class using the `from...import` statement.

```python
from stock import Stock
```

5. After importing the `Stock` class, we can create a `Stock` object. An object is an instance of a class. We'll create a `Stock` object with the name `GOOG`, 100 shares, and a price of `490.10`. Then we'll print the name of the stock and calculate its cost using the `cost()` method.

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

6. Finally, when we're done using the Python interpreter, we can exit it using the `exit()` function.

```python
exit()
```

This lab has demonstrated two different ways to import Python code:

- `import module_name` - This imports the entire module, making all the functions, classes, and variables in that module available for use.
- `from module_name import specific_item` - This imports only a specific item (like a class or a function) from the module, which can be useful if you only need a part of the module's functionality.
