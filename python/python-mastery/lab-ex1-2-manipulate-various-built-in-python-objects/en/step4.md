# Working with Python Dictionaries

In Python, dictionaries are a fundamental data structure. They are key - value stores, which means they allow you to map one value (the value) to another (the key). This is extremely useful when dealing with data that has natural key - value relationships. For example, you might want to map a person's name (the key) to their age (the value), or as we'll see in this lab, map stock symbols (keys) to their prices (values).

## Creating and Accessing Dictionaries

Let's start by opening a new Python interactive session. This is like entering a special environment where you can write and run Python code line by line. To start this session, open your terminal and type the following command:

```bash
python3
```

Once you're in the Python interactive session, you can create a dictionary. In our case, we'll create a dictionary that maps stock symbols to their prices. Here's how you do it:

```python
>>> prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
>>> prices
{'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
```

In the first line, we're creating a dictionary named `prices` and assigning it some key - value pairs. The keys are the stock symbols (`IBM`, `GOOG`, `AAPL`), and the values are the corresponding prices. The second line just shows us the contents of the `prices` dictionary.

Now, let's see how to access and modify the values in the dictionary using the keys.

```python
>>> prices['IBM']    # Access the value for key 'IBM'
91.1

>>> prices['IBM'] = 123.45    # Update an existing value
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23}

>>> prices['HPQ'] = 26.15    # Add a new key - value pair
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23, 'HPQ': 26.15}
```

In the first line, we're accessing the value associated with the key `IBM`. In the second and third lines, we're updating the value for the key `IBM` and then adding a new key - value pair (`HPQ` with a price of `26.15`).

## Getting Dictionary Keys

Sometimes, you might want to get a list of all the keys in a dictionary. There are a couple of ways to do this.

```python
>>> list(prices)    # Convert dictionary keys to a list
['IBM', 'GOOG', 'AAPL', 'HPQ']
```

Here, we're using the `list()` function to convert the keys of the `prices` dictionary into a list.

You can also use the `keys()` method, which returns a special object called `dict_keys`.

```python
>>> prices.keys()    # Returns a dict_keys object
dict_keys(['IBM', 'GOOG', 'AAPL', 'HPQ'])
```

## Getting Dictionary Values

Similarly, you might want to get all the values in a dictionary. You can use the `values()` method for this.

```python
>>> prices.values()    # Returns a dict_values object
dict_values([123.45, 490.1, 312.23, 26.15])
```

This method returns a `dict_values` object that contains all the values in the `prices` dictionary.

## Deleting Items

If you want to remove a key - value pair from a dictionary, you can use the `del` keyword.

```python
>>> del prices['AAPL']    # Delete the 'AAPL' entry
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'HPQ': 26.15}
```

Here, we're deleting the key - value pair with the key `AAPL` from the `prices` dictionary.

## Checking if a Key Exists

To check if a key exists in a dictionary, you can use the `in` operator.

```python
>>> 'IBM' in prices
True
>>> 'AAPL' in prices
False
```

The `in` operator returns `True` if the key exists in the dictionary and `False` otherwise.

## Dictionary Methods

Dictionaries have several useful methods. Let's look at a couple of them.

```python
>>> prices.get('MSFT', 0)    # Get value or default if key doesn't exist
0
>>> prices.get('IBM', 0)
123.45

>>> prices.update({'MSFT': 25.0, 'GOOG': 500.0})    # Update multiple values
>>> prices
{'IBM': 123.45, 'GOOG': 500.0, 'HPQ': 26.15, 'MSFT': 25.0}
```

The `get()` method tries to get the value associated with a key. If the key doesn't exist, it returns a default value (in this case, `0`). The `update()` method is used to update multiple key - value pairs in the dictionary at once.

When you're done working in the Python interactive session, you can exit it by typing:

```python
>>> exit()
```
