# Working with Python Numbers

Python provides powerful support for numerical operations. This step introduces basic number manipulation.

## Basic Arithmetic Operations

Open a Python interactive shell by typing `python3` in your terminal:

```bash
python3
```

Try some basic arithmetic operations:

```python
>>> 3 + 4*5    # Multiplication has higher precedence than addition
23
>>> 23.45 / 1e-02    # Scientific notation for 0.01
2345.0
```

## Integer Division

Python 3 handles division differently from Python 2:

```python
>>> 7 / 4    # In Python 3, regular division returns a float
1.75
>>> 7 // 4   # Floor division (truncates the decimal part)
1
```

## Number Methods

Numbers in Python have several useful methods that are often overlooked. Let's explore some of them:

```python
>>> x = 1172.5
>>> x.as_integer_ratio()    # Represents the float as a fraction
(2345, 2)
>>> x.is_integer()    # Checks if the float is an integer value
False

>>> y = 12345
>>> y.numerator    # For integers, numerator is the number itself
12345
>>> y.denominator    # For integers, denominator is always 1
1
>>> y.bit_length()    # Number of bits required to represent the number
14
```

These methods are particularly useful when you need to perform specific numerical operations or conversions.

Exit the Python shell when you're done by typing:

```python
>>> exit()
```
