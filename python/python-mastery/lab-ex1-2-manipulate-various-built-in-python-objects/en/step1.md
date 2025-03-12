# Working with Python Numbers

Python offers robust support for numerical operations. In programming, numbers are fundamental data types used for calculations and representing quantities. This step will introduce you to basic number manipulation in Python, which is essential for performing various mathematical operations in your programs.

## Basic Arithmetic Operations

To start working with Python numbers, you first need to open a Python interactive shell. You can do this by typing `python3` in your terminal. The Python interactive shell allows you to write and execute Python code line by line, which is great for testing and learning.

```bash
python3
```

Once you're in the Python interactive shell, you can try some basic arithmetic operations. Python follows the standard mathematical rules for arithmetic, such as the order of operations (PEMDAS: Parentheses, Exponents, Multiplication and Division, Addition and Subtraction).

```python
>>> 3 + 4*5    # Multiplication has higher precedence than addition, so 4*5 is calculated first, then added to 3
23
>>> 23.45 / 1e-02    # Scientific notation for 0.01 is used here. Division is performed to get the result
2345.0
```

## Integer Division

Python 3 handles division differently from Python 2. Understanding these differences is crucial to avoid unexpected results in your code.

```python
>>> 7 / 4    # In Python 3, regular division returns a float, even if the result could be an integer
1.75
>>> 7 // 4   # Floor division (truncates the decimal part) gives you the quotient as an integer
1
```

## Number Methods

Numbers in Python have several useful methods that are often overlooked. These methods can simplify complex numerical operations and conversions. Let's explore some of them:

```python
>>> x = 1172.5
>>> x.as_integer_ratio()    # This method represents the float as a fraction, which can be useful for some mathematical calculations
(2345, 2)
>>> x.is_integer()    # Checks if the float is an integer value. In this case, 1172.5 is not an integer, so it returns False
False

>>> y = 12345
>>> y.numerator    # For integers, the numerator is the number itself
12345
>>> y.denominator    # For integers, the denominator is always 1
1
>>> y.bit_length()    # This method tells you the number of bits required to represent the number in binary, which can be useful in bitwise operations
14
```

These methods are particularly useful when you need to perform specific numerical operations or conversions. They can save you time and make your code more efficient.

When you're done exploring the Python interactive shell, you can exit it by typing:

```python
>>> exit()
```
