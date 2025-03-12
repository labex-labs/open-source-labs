# Working with Python Lists

Lists are versatile data structures in Python that can store collections of items. In this step, we'll explore list operations.

## Creating Lists from Strings

Start a new Python interactive session:

```bash
python3
```

Define a string of stock symbols and convert it to a list:

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # Split the string on whitespace
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

## Accessing and Modifying List Elements

Lists support indexing like strings, but unlike strings, list elements can be modified:

```python
>>> symlist[0]    # First element
'HPQ'
>>> symlist[1]    # Second element
'AAPL'
>>> symlist[-1]   # Last element
'GOOG'
>>> symlist[-2]   # Second to last element
'YHOO'

>>> symlist[2] = 'AIG'    # Replace the third element
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
```

## Iterating Through Lists

The `for` loop is commonly used to process each element in a list:

```python
>>> for s in symlist:
...     print('s =', s)
...
```

You should see the following output:

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## Checking Membership

Use the `in` operator to check if an item exists in a list:

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## Adding and Removing Elements

Lists have methods to add and remove elements:

```python
>>> symlist.append('RHT')    # Add an element to the end
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.insert(1, 'AA')    # Insert at specific position
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.remove('MSFT')    # Remove by value
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Try removing an element that doesn't exist:

```python
>>> symlist.remove('MSFT')
```

You should see an error like:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

Find the position of an element:

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # Verify the element at that position
'YHOO'
```

## Sorting Lists

Lists can be sorted in place:

```python
>>> symlist.sort()    # Sort alphabetically
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # Sort in reverse
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## Nested Lists

Lists can contain any type of object, including other lists:

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Accessing elements in nested lists:

```python
>>> items[0]    # First element (the symlist)
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]    # Second element in symlist
'RHT'
>>> items[0][1][2]    # Third character in 'RHT'
'T'
>>> items[1]    # Second element (the nums list)
[101, 102, 103]
>>> items[1][1]    # Second element in nums
102
```

Exit the Python shell when you're done:

```python
>>> exit()
```
