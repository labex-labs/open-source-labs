# Creating Stock Objects

Now that we have defined our `Stock` class, it's time to put it into action. Creating instances of a class is like making specific examples based on a general blueprint. In this case, the `Stock` class is our blueprint, and we'll create some stock objects. After creating these objects, we'll learn how to access their attributes (characteristics) and methods (actions they can perform).

1. First, we need to open a terminal in the WebIDE. The terminal is like a command - center where we can give instructions to our computer. To open it, click on "Terminal" in the menu.

2. Once the terminal is open, we need to make sure we are in the correct project directory. The project directory is where all the relevant files for our project are stored. If you are not already in the project directory, use the following command to navigate there:

```bash
cd /home/labex/project
```

3. Now, we want to start Python in interactive mode with our `stock.py` file. Interactive mode allows us to test our code step - by - step and see the results immediately. The `stock.py` file contains the definition of our `Stock` class. Use the following command:

```bash
python3 -i stock.py
```

The `-i` flag is important here. It tells Python to run the `stock.py` script first. After running the script, it starts an interactive session. In this session, we can access any classes and variables that were defined in the `stock.py` script.

4. Let's create a new `Stock` object for Google stock. Creating an object is like making a specific instance of the `Stock` class with particular values. Use the following code:

```python
s = Stock('GOOG', 100, 490.10)
```

This line of code creates a new instance of the `Stock` class. Here's what each value means:

- Name: 'GOOG' - This is the symbol for Google stock.
- Shares: 100 - It represents the number of shares of Google stock we have.
- Price: 490.10 - This is the price per share of Google stock.

5. Now that we have our `Stock` object, we can access its attributes. Attributes are like the properties of an object. To access an attribute, we use the object's name followed by a dot and the attribute name.

```python
s.name
```

When you run this code, it will output the name of the stock:

```
'GOOG'
```

Let's access the number of shares:

```python
s.shares
```

The output will be the number of shares we defined:

```
100
```

Finally, let's access the price per share:

```python
s.price
```

The output will be the price per share:

```
490.1
```

6. Our `Stock` class has a method called `cost()`. A method is like an action that an object can perform. In this case, the `cost()` method calculates the total cost of our shares. To call this method, use the following code:

```python
s.cost()
```

The output will be the total cost:

```
49010.0
```

The `cost()` method works by multiplying the number of shares (100) by the price per share (490.10), which gives us 49010.0.
