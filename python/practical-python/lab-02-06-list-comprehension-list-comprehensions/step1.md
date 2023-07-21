# Creating new lists

A list comprehension creates a new list by applying an operation to
each element of a sequence.

```python
>>> a = [1, 2, 3, 4, 5]
>>> b = [2*x for x in a ]
>>> b
[2, 4, 6, 8, 10]
>>>
```

Another example:

```python
>>> names = ['Elwood', 'Jake']
>>> a = [name.lower() for name in names]
>>> a
['elwood', 'jake']
>>>
```

The general syntax is: `[ <expression> for <variable_name> in <sequence> ]`.
