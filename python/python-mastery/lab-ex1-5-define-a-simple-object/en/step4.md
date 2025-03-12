# Working with Multiple Stock Objects

We can create multiple instances of our `Stock` class to represent different stocks. Each instance will maintain its own set of attributes.

1. With the Python interactive session still running, create another `Stock` object for IBM:

```python
t = Stock('IBM', 50, 91.5)
```

2. Calculate the cost of this new stock:

```python
t.cost()
```

Output:

```
4575.0
```

3. We can format and display our stock information using Python's string formatting:

```python
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
```

Output:

```
      GOOG        100     490.10
```

This formatted string works as follows:

- `%10s` formats a string in a field 10 characters wide (right-aligned)
- `%10d` formats an integer in a field 10 characters wide
- `%10.2f` formats a float with 2 decimal places in a field 10 characters wide

4. Format the IBM stock information the same way:

```python
print('%10s %10d %10.2f' % (t.name, t.shares, t.price))
```

Output:

```
       IBM         50      91.50
```

5. Compare the costs of both stocks using f-strings, a more modern Python formatting method:

```python
print(f"Google stock costs ${s.cost()}, IBM stock costs ${t.cost()}")
```

Output:

```
Google stock costs $49010.0, IBM stock costs $4575.0
```

6. When you are finished experimenting, exit the Python interactive mode:

```python
exit()
```

Each Stock object maintains its own set of attributes, which demonstrates how class instances work in object-oriented programming. This allows us to create multiple stock objects, each with different values, while sharing the same methods.
