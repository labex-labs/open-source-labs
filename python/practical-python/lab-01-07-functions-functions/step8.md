# Exercise 1.31: Error handling

What happens if you try your function on a file with some missing fields?

```python
>>> portfolio_cost('Data/missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

At this point, you're faced with a decision. To make the program work you can either sanitize the original input file by eliminating bad lines or you can modify your code to handle the bad lines in some manner.

Modify the `pcost.py` program to catch the exception, print a warning message, and continue processing the rest of the file.
