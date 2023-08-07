# Returning Optional Values

Sometimes a function might return an optional value--possibly as a mechanism for indicating success or failure. The most common convention is to use `None` as a representation for a missing value. Modify the `parse_line()` function above so that it either returns a tuple on success or `None` on bad data. For example:

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> parse_line('spam')       # Returns None
>>>
```

Design discussion: Would it be better for the `parse_line()` function to raise an exception on malformed data?
