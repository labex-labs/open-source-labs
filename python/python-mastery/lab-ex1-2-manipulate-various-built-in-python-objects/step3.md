# Part 3 : List Manipulation

In the first part, you worked with strings containing stock symbols. For example:

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```

Define the above variable and split it into a list of names using the `split()` operation of strings:

```python
>>> symlist = symbols.split()
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## Extracting and reassigning list elements

Lists work like arrays where you can look up and modify elements by numerical index. Try a few lookups:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'YHOO'
>>>
```

Try reassigning one of the items:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## Looping over list items

The `for` loop works by looping over data in a sequence such as a list. Check this out by typing the following loop and watching what happens:

```python
>>> for s in symlist:
        print('s =', s)

... look at the output ...
```

## Membership tests

Use the `in` operator to check if `'AIG'`,`'AA'`, and `'CAT'` are in the list of symbols.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>>
```

## Appending, inserting, and deleting items

Use the `append()` method to add the symbol `'RHT'` to end of `symlist`.

```python
>>> symlist.append('RHT')
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Use the `insert()` method to insert the symbol `'AA'` as the second item in the list.

```python
>>> symlist.insert(1,'AA')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Use the `remove()` method to remove `'MSFT'` from the list.

```python
>>> symlist.remove('MSFT')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Try calling `remove()` again to see what happens if the item can't be found.

```python
>>> symlist.remove('MSFT')
... watch what happens ...
>>>
```

Use the `index()` method to find the position of `'YHOO'` in the list.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]
'YHOO'
>>>
```

## List sorting

Want to sort a list? Use the `sort()` method. Try it out:

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

Want to sort in reverse? Try this:

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

Note: Sorting a list modifies its contents "in-place." That is, the elements of the list are shuffled around, but no new list is created as a result.

## Lists of anything

Lists can contain any kind of object, including other lists (e.g., nested lists). Try this out:

```python
>>> nums = [101,102,103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Pay close attention to the above output. `items` is a list with two elements. Each element is list.

Try some nested list lookups:

```python
>>> items[0]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]
'RHT'
>>> items[0][1][2]
'T'
>>> items[1]
[101, 102, 103]
>>> items[1][1]
102
>>>
```
