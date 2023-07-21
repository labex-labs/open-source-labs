# Exercise 1.18: Regular Expressions

One limitation of the basic string operations is that they don't
support any kind of advanced pattern matching. For that, you
need to turn to Python's `re` module and regular expressions.
Regular expression handling is a big topic, but here is a short
example:

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Find all occurrences of a date
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Replace all occurrences of a date with replacement text
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

For more information about the `re` module, see the official documentation at
[https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).
