# Performing Operations with Nullable Integer Arrays

You can perform various operations with nullable integer arrays, such as arithmetic operations, comparisons, and slicing.

```python
# Create a Series with nullable integer type
s = pd.Series([1, 2, None], dtype="Int64")

# Perform arithmetic operation
s_plus_one = s + 1 # adds 1 to each element in the series

# Perform comparison
comparison = s == 1 # checks if each element in the series is equal to 1

# Perform slicing operation
sliced = s.iloc[1:3] # selects the second and third elements in the series
```
