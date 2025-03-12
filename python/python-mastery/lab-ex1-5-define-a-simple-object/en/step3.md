# Creating Stock Objects

Now that we have defined our `Stock` class, let's create some instances and learn how to access their attributes and methods.

1. Open a terminal in the WebIDE by clicking on "Terminal" in the menu.

2. Navigate to the project directory if you are not already there:

```bash
cd /home/labex/project
```

3. Launch Python in interactive mode with our `stock.py` file:

```bash
python3 -i stock.py
```

The `-i` flag tells Python to run the script and then start an interactive session, giving us access to any classes and variables defined in the script.

4. Create a new `Stock` object for Google stock:

```python
s = Stock('GOOG', 100, 490.10)
```

This creates a new instance of the `Stock` class with the following values:

- Name: 'GOOG'
- Shares: 100
- Price: 490.10

5. Access the attributes of your stock object:

```python
s.name
```

Output:

```
'GOOG'
```

```python
s.shares
```

Output:

```
100
```

```python
s.price
```

Output:

```
490.1
```

6. Call the `cost()` method to calculate the total cost:

```python
s.cost()
```

Output:

```
49010.0
```

The `cost()` method multiplies shares (100) by price (490.10) to give us 49010.0.
