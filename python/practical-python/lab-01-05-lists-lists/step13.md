# Exercise 1.25: Lists of anything

Lists can contain any kind of object, including other lists (e.g., nested lists).
Try this out:

```python
>>> nums = [101, 102, 103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Pay close attention to the above output. `items` is a list with three elements.
The first element is a string, but the other two elements are lists.

You can access items in the nested lists by using multiple indexing operations.

```python
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
```

Even though it is technically possible to make very complicated list
structures, as a general rule, you want to keep things simple.
Usually lists hold items that are all the same kind of value. For
example, a list that consists entirely of numbers or a list of text
strings. Mixing different kinds of data together in the same list is
often a good way to make your head explode so it's best avoided.
