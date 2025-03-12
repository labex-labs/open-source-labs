# Working with Python Lists

Lists are a type of data structure in Python. A data structure is a way to organize and store data so that it can be used efficiently. Lists are very versatile because they can store different types of items, like numbers, strings, or even other lists. In this step, we'll learn how to perform various operations on lists.

## Creating Lists from Strings

To start working with Python lists, we first need to open a Python interactive session. This is like a special environment where we can write and run Python code right away. To start this session, type the following command in your terminal:

```bash
python3
```

Once you're in the Python interactive session, we'll create a list from a string. A string is just a sequence of characters. We'll define a string that contains some stock symbols separated by spaces. Then, we'll convert this string into a list. Each stock symbol will become an element in the list.

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # Split the string on whitespace
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

The `split()` method is used to break the string into parts wherever there is a whitespace. Each part then becomes an element in the new list.

## Accessing and Modifying List Elements

Just like strings, lists support indexing. Indexing means we can access individual elements in the list by their position. In Python, the first element in a list has an index of 0, the second has an index of 1, and so on. We can also use negative indexing to access elements from the end of the list. The last element has an index of -1, the second last has an index of -2, and so on.

Unlike strings, list elements can be modified. This means we can change the value of an element in the list.

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

Often, we need to perform the same operation on each element in a list. We can use a `for` loop to do this. A `for` loop allows us to go through each element in the list one by one and perform a specific action on it.

```python
>>> for s in symlist:
...     print('s =', s)
...
```

When you run this code, you'll see each element in the list printed out with the label `s =`.

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## Checking Membership

Sometimes, we need to check if a particular item exists in a list. We can use the `in` operator to do this. The `in` operator returns `True` if the item is in the list and `False` if it's not.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## Adding and Removing Elements

Lists have built - in methods that allow us to add and remove elements. The `append()` method adds an element to the end of the list. The `insert()` method inserts an element at a specific position in the list. The `remove()` method removes an element from the list by its value.

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

If you try to remove an element that doesn't exist in the list, Python will raise an error.

```python
>>> symlist.remove('MSFT')
```

You'll see an error message like this:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

We can also find the position of an element in the list using the `index()` method.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # Verify the element at that position
'YHOO'
```

## Sorting Lists

Lists can be sorted in place, which means the original list is modified. We can sort a list alphabetically or in reverse order.

```python
>>> symlist.sort()    # Sort alphabetically
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # Sort in reverse
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## Nested Lists

Lists can contain any type of object, including other lists. This is called a nested list.

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

To access elements in a nested list, we use multiple indices. The first index selects the outer list element, and the second index selects the inner list element.

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

When you're done working in the Python interactive session, you can exit it by typing:

```python
>>> exit()
```
