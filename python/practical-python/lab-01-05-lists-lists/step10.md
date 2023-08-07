# Exercise 1.22: Appending, inserting, and deleting items

Use the `append()` method to add the symbol `'RHT'` to end of `symlist`.

```python
>>> # append 'RHT'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Use the `insert()` method to insert the symbol `'AA'` as the second item in the list.

```python
>>> # Insert 'AA' as the second item in the list
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Use the `remove()` method to remove `'MSFT'` from the list.

```python
>>> # Remove 'MSFT'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

Append a duplicate entry for `'YHOO'` at the end of the list.

_Note: it is perfectly fine for a list to have duplicate values._

```python
>>> # Append 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

Use the `index()` method to find the first position of `'YHOO'` in the list.

```python
>>> # Find the first index of 'YHOO'
4
>>> symlist[4]
'YHOO'
>>>
```

Count how many times `'YHOO'` is in the list:

```python
>>> symlist.count('YHOO')
2
>>>
```

Remove the first occurrence of `'YHOO'`.

```python
>>> # Remove first occurrence 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

Just so you know, there is no method to find or remove all occurrences of an item. However, we'll see an elegant way to do this in section 2.
