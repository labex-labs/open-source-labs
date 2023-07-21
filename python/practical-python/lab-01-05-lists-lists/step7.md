# Exercise 1.19: Extracting and reassigning list elements

Try a few lookups:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

Try reassigning one value:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

Take a few slices:

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

Create an empty list and append an item to it.

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

You can reassign a portion of a list to another list. For example:

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

When you do this, the list on the left-hand-side (`symlist`) will be resized as appropriate to make the right-hand-side (`mysyms`) fit.
For instance, in the above example, the last two items of `symlist` got replaced by the single item in the list `mysyms`.
