# Working with Python Strings

Strings are one of the most commonly used data types in Python. In this step, we'll explore various string operations.

## Creating and Defining Strings

Open a Python interactive shell again:

```bash
python3
```

Define a string containing stock ticker symbols:

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
>>> symbols
'AAPL IBM MSFT YHOO SCO'
```

## Accessing Characters and Substrings

Strings in Python can be indexed to access individual characters, where indexing starts at 0:

```python
>>> symbols[0]    # First character
'A'
>>> symbols[1]    # Second character
'A'
>>> symbols[2]    # Third character
'P'
>>> symbols[-1]   # Last character
'O'
>>> symbols[-2]   # Second to last character
'C'
```

You can also extract substrings using slicing:

```python
>>> symbols[:4]    # First 4 characters
'AAPL'
>>> symbols[-3:]   # Last 3 characters
'SCO'
>>> symbols[5:8]   # Characters from index 5 to 7
'IBM'
```

## String Immutability

Strings in Python are immutable, meaning you cannot change individual characters:

```python
>>> symbols[0] = 'a'    # This will cause an error
```

You should see an error like:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## String Concatenation

Although you cannot modify strings directly, you can create new strings through concatenation:

```python
>>> symbols += ' GOOG'    # Append a new symbol
>>> symbols
'AAPL IBM MSFT YHOO SCO GOOG'

>>> symbols = 'HPQ ' + symbols    # Prepend a new symbol
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

Remember, these operations create new strings rather than modifying the original.

## Testing for Substrings

Use the `in` operator to check if a substring exists within a string:

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

Notice that 'AA' returns `True` because it's found within "AAPL".

## String Methods

Python strings come with numerous built-in methods:

```python
>>> symbols.lower()    # Convert to lowercase
'hpq aapl ibm msft yhoo sco goog'

>>> symbols    # Original string remains unchanged
'HPQ AAPL IBM MSFT YHOO SCO GOOG'

>>> lowersyms = symbols.lower()    # Save the result to a new variable
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'

>>> symbols.find('MSFT')    # Find the starting index of a substring
13
>>> symbols[13:17]    # Verify the substring at that position
'MSFT'

>>> symbols = symbols.replace('SCO','')    # Replace a substring
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
```

When you're done experimenting, you can exit the Python shell:

```python
>>> exit()
```
