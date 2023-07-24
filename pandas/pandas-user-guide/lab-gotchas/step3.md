# Mutating with User Defined Function (UDF) Methods

When using a pandas method that takes a UDF, avoid changing the DataFrame inside the UDF. Instead, make a copy before making changes.

```python
def f(s):
    s = s.copy()
    s.pop("a")
    return s

df = pd.DataFrame({"a": [1, 2, 3], 'b': [4, 5, 6]})
df.apply(f, axis="columns")
```
