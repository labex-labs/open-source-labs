# Dictionary Lookups

You can test the existence of a key.

```python
if key in d:
    # YES
else:
    # NO
```

You can look up a value that might not exist and provide a default value in case it doesn't.

```python
name = d.get(key, default)
```

An example:

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```
