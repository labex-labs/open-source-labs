# Slicing

Slicing means to take a subsequence from a sequence. The syntax is `s[start:end]`. Where `start` and `end` are the indexes of the subsequence you want.

```python
a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]
```

- Indices `start` and `end` must be integers.
- Slices do _not_ include the end value. It is like a half-open interval from math.
- If indices are omitted, they default to the beginning or end of the list.
