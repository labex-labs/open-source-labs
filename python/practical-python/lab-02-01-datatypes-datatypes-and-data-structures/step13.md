# Exercise 2.3: Some additional dictionary operations

If you turn a dictionary into a list, you’ll get all of its keys:

```python
>>> list(d)
['name', 'shares', 'price', 'date', 'account']
>>>
```

Similarly, if you use the `for` statement to iterate on a dictionary,
you will get the keys:

```python
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

Try this variant that performs a lookup at the same time:

```python
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

You can also obtain all of the keys using the `keys()` method:

```python
>>> keys = d.keys()
>>> keys
dict_keys(['name', 'shares', 'price', 'date', 'account'])
>>>
```

`keys()` is a bit unusual in that it returns a special `dict_keys` object.

This is an overlay on the original dictionary that always gives you
the current keys—even if the dictionary changes. For example, try
this:

```python
>>> del d['account']
>>> keys
dict_keys(['name', 'shares', 'price', 'date'])
>>>
```

Carefully notice that the `'account'` disappeared from `keys` even
though you didn’t call `d.keys()` again.

A more elegant way to work with keys and values together is to use the
`items()` method. This gives you `(key, value)` tuples:

```python
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

If you have tuples such as `items`, you can create a dictionary using
the `dict()` function. Try it:

```python
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```
