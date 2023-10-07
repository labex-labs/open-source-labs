# Exercise 1.17: f-strings

Sometimes you want to create a string and embed the values of variables into it.

To do that, use an f-string. For example:

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'
>>>
```

Modify the `mortgage.py` program from Exercise 1.10 to create its output using f-strings. Try to make it so that output is nicely aligned.
