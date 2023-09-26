# Collection is empty

Write a Python function called `is_empty(val)` that takes a value as its parameter and returns `True` if the value is an empty sequence or collection, and `False` otherwise.

To check if a sequence or collection is empty, you can use the `not` operator to test the truth value of the provided sequence or collection. If the sequence or collection is empty, the `not` operator will return `True`.

Your function should be able to handle the following types of sequences and collections:

- Lists
- Tuples
- Sets
- Dictionaries
- Strings
- Ranges

```python
def is_empty(val):
  return not val
```

```python
is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```
