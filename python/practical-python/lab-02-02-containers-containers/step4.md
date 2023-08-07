# Dicts as a Container

Dictionaries are useful if you want fast random lookups (by key name). For example, a dictionary of stock prices:

```python
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
```

Here are some simple lookups:

```python
>>> prices['IBM']
93.37
>>> prices['GOOG']
513.25
>>>
```
