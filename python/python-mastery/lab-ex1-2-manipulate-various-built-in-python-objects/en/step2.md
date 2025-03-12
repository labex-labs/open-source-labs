# Working with Python Strings

Strings are one of the most commonly used data types in Python. They are used to represent text and can contain letters, numbers, and symbols. In this step, we'll explore various string operations, which are essential skills for working with text data in Python.

## Creating and Defining Strings

To start working with strings in Python, we first need to open a Python interactive shell. This shell allows us to write and execute Python code line by line, which is great for learning and testing. Open a Python interactive shell again using the following command:

```bash
python3
```

Once the shell is open, we can define a string. In this example, we'll create a string that contains stock ticker symbols. A string in Python can be defined by enclosing text within single quotes (`'`) or double quotes (`"`). Here's how we define our string:

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
>>> symbols
'AAPL IBM MSFT YHOO SCO'
```

We've now created a string variable named `symbols` and assigned it a value. When we type the variable name and press enter, Python displays the value of the string.

## Accessing Characters and Substrings

In Python, strings can be indexed to access individual characters. Indexing starts at 0, which means the first character of a string has an index of 0, the second has an index of 1, and so on. Negative indexing is also supported, where -1 refers to the last character, -2 refers to the second last character, and so on.

Let's see how we can access individual characters in our `symbols` string:

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

We can also extract substrings using slicing. Slicing allows us to get a part of the string by specifying a start and an end index. The syntax for slicing is `string[start:end]`, where the substring includes characters from the start index up to (but not including) the end index.

```python
>>> symbols[:4]    # First 4 characters
'AAPL'
>>> symbols[-3:]   # Last 3 characters
'SCO'
>>> symbols[5:8]   # Characters from index 5 to 7
'IBM'
```

## String Immutability

Strings in Python are immutable, which means once a string is created, you cannot change its individual characters. If you try to modify a character in a string, Python will raise an error.

Let's try to change the first character of our `symbols` string:

```python
>>> symbols[0] = 'a'    # This will cause an error
```

You should see an error like this:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

This error indicates that we cannot assign a new value to an individual character in a string because strings are immutable.

## String Concatenation

Although we cannot modify strings directly, we can create new strings through concatenation. Concatenation means joining two or more strings together. In Python, we can use the `+` operator to concatenate strings.

```python
>>> symbols += ' GOOG'    # Append a new symbol
>>> symbols
'AAPL IBM MSFT YHOO SCO GOOG'

>>> symbols = 'HPQ ' + symbols    # Prepend a new symbol
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

It's important to remember that these operations create new strings rather than modifying the original string. The original string remains unchanged, and a new string is created with the combined value.

## Testing for Substrings

To check if a substring exists within a string, we can use the `in` operator. The `in` operator returns `True` if the substring is found in the string and `False` otherwise.

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

Notice that 'AA' returns `True` because it's found within "AAPL". This is a useful way to search for specific text within a larger string.

## String Methods

Python strings come with numerous built-in methods that allow us to perform various operations on strings. These methods are functions that are associated with the string object and can be called using the dot notation (`string.method()`).

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

When you're done experimenting, you can exit the Python shell using the following command:

```python
>>> exit()
```
