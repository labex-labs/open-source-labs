# Sets

Sets are collection of unordered unique items.

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# Alternative syntax
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

Sets are useful for membership tests.

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

Sets are also useful for duplicate elimination.

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

Additional set operations:

```python
unique.add('CAT')        # Add an item
unique.remove('YHOO')    # Remove an item

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # Set union { 'a', 'b', 'c', 'd' }
s1 & s2                 # Set intersection { 'c' }
s1 - s2                 # Set difference { 'a', 'b' }
```

In these exercises, you start building one of the major programs used for the rest of this course. Do your work in the file `Work/report.py`.
