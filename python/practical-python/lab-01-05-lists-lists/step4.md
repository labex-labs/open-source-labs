# List Removal

You can remove items either by element value or by index:

```python
# Using the value
names.remove('Curtis')

# Using the index
del names[1]
```

Removing an item does not create a hole. Other items will move down to fill the space vacated. If there are more than one occurrence of the element, `remove()` will remove only the first occurrence.
