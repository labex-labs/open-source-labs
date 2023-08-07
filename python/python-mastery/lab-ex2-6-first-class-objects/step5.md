# Deep Thought

In this exercise, you have written two functions, `read_csv_as_dicts()` and
`read_csv_as_columns()`. These functions present data to the user in the same way.
For example:

```python
>>> data1 = read_csv_as_dicts('ctabus.csv', [str, str, str, int])
>>> len(data1)
577563
>>> data1[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data1[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>

>>> data2 = read_csv_as_columns('ctabus.csv', [str, str, str, int])
>>> len(data2)
577563
>>> data2[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data2[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```

In fact, you can use either function in the CTA data analysis code
that you wrote. Yet, under the covers completely different things are
happening. The `read_csv_as_columns()` function is storing the data
in a different representation. It's relying on Python sequence
protocols (magic methods) to present information to you in a more useful
way.

This is really part of a much bigger programming concept of "Data
Abstraction". When writing programs, the way in which data is
presented is often more important than how the data is actually put
together under the hood. Although we're presenting the data as a
sequence of dictionaries, there's a great deal of flexibility in
how that actually happens behind the scenes. That's a powerful
idea and something to think about when writing your own programs.
