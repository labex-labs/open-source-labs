# Use String Methods

Pandas provides a suite of string processing methods that make it easy to operate on string data. These methods automatically exclude missing/NA values.

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# convert to lowercase
s.str.lower()

# convert to uppercase
s.str.upper()

# calculate the length of each string
s.str.len()
```
