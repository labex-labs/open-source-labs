# Working with Multiple Stock Objects

In object - oriented programming, a class is like a blueprint, and instances of that class are the actual objects created based on that blueprint. Our `Stock` class is a blueprint for representing stocks. We can create multiple instances of this `Stock` class to represent different stocks. Each instance will have its own set of attributes, such as the stock name, the number of shares, and the price per share.

1. With the Python interactive session still running, we are going to create another `Stock` object. This time, it will represent IBM. To create an instance of the `Stock` class, we call the class name as if it were a function and pass in the necessary arguments. The arguments here are the stock name, the number of shares, and the price per share.

```python
t = Stock('IBM', 50, 91.5)
```

In this line of code, we are creating a new `Stock` object named `t` that represents IBM. It has 50 shares, and each share costs $91.5.

2. Now, we want to calculate the cost of this new stock. The `Stock` class has a method named `cost()` that calculates the total cost of the stock by multiplying the number of shares by the price per share.

```python
t.cost()
```

When you run this code, Python will call the `cost()` method on the `t` object and return the total cost.

Output:

```
4575.0
```

3. We can format and display our stock information in a nice, organized way using Python's string formatting. String formatting allows us to specify how different types of data should be presented in a string.

```python
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
```

In this code, we are using the old - style string formatting in Python. The `%` operator is used to substitute values into a string template. The string template `'%10s %10d %10.2f'` defines how the stock name, number of shares, and price should be formatted.

Output:

```
      GOOG        100     490.10
```

This formatted string works as follows:

- `%10s` formats a string in a field 10 characters wide (right - aligned). This means that the stock name will be placed in a space that is 10 characters wide, and it will be right - aligned within that space.
- `%10d` formats an integer in a field 10 characters wide. So, the number of shares will be placed in a 10 - character - wide space.
- `%10.2f` formats a float with 2 decimal places in a field 10 characters wide. The price will be shown with two decimal places and placed in a 10 - character - wide space.

4. Now, let's format the IBM stock information in the same way. We just need to replace the object name from `s` to `t` in the string formatting code.

```python
print('%10s %10d %10.2f' % (t.name, t.shares, t.price))
```

Output:

```
       IBM         50      91.50
```

5. In modern Python, we can also use f - strings for formatting. F - strings are more readable and easier to use. Let's compare the costs of both stocks using f - strings.

```python
print(f"Google stock costs ${s.cost()}, IBM stock costs ${t.cost()}")
```

In this f - string, we are directly embedding expressions inside curly braces `{}`. Python will evaluate these expressions and insert the results into the string.

Output:

```
Google stock costs $49010.0, IBM stock costs $4575.0
```

6. When you are finished experimenting, it's time to exit the Python interactive mode. You can do this by using the `exit()` function.

```python
exit()
```

Each Stock object maintains its own set of attributes, which demonstrates how class instances work in object - oriented programming. This allows us to create multiple stock objects, each with different values, while sharing the same methods.
