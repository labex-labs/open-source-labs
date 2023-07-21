# String Indexing

Strings work like an array for accessing individual characters. You use an integer index, starting at 0.
Negative indices specify a position relative to the end of the string.

```python
a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (end of string)
```

You can also slice or select substrings specifying a range of indices with `:`.

```python
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
```

The character at the ending index is not included. Missing indices assume the beginning or ending of the string.
