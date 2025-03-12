# Working with Python Dictionaries

Dictionaries are key-value stores that allow you to map one value to another. They're extremely useful for data that has natural key-value relationships.

## Creating and Accessing Dictionaries

Start a new Python interactive session:

```bash
python3
```

Create a dictionary mapping stock symbols to their prices:

```python
>>> prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
>>> prices
{'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
```

Access and modify dictionary values using keys:

```python
>>> prices['IBM']    # Access the value for key 'IBM'
91.1

>>> prices['IBM'] = 123.45    # Update an existing value
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23}

>>> prices['HPQ'] = 26.15    # Add a new key-value pair
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23, 'HPQ': 26.15}
```

## Getting Dictionary Keys

To get a list of all keys in a dictionary:

```python
>>> list(prices)    # Convert dictionary keys to a list
['IBM', 'GOOG', 'AAPL', 'HPQ']
```

You can also use the `keys()` method:

```python
>>> prices.keys()    # Returns a dict_keys object
dict_keys(['IBM', 'GOOG', 'AAPL', 'HPQ'])
```

## Getting Dictionary Values

To get all values in a dictionary:

```python
>>> prices.values()    # Returns a dict_values object
dict_values([123.45, 490.1, 312.23, 26.15])
```

## Deleting Items

To remove a key-value pair from a dictionary:

```python
>>> del prices['AAPL']    # Delete the 'AAPL' entry
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'HPQ': 26.15}
```

## Checking if a Key Exists

Use the `in` operator to check if a key exists:

```python
>>> 'IBM' in prices
True
>>> 'AAPL' in prices
False
```

## Dictionary Methods

Dictionaries have several useful methods:

```python
>>> prices.get('MSFT', 0)    # Get value or default if key doesn't exist
0
>>> prices.get('IBM', 0)
123.45

>>> prices.update({'MSFT': 25.0, 'GOOG': 500.0})    # Update multiple values
>>> prices
{'IBM': 123.45, 'GOOG': 500.0, 'HPQ': 26.15, 'MSFT': 25.0}
```

Exit the Python shell when you're done:

```python
>>> exit()
```
