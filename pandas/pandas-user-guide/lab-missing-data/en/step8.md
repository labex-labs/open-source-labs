# Understand NA Scalar to Denote Missing Values

Finally, we'll discuss the experimental `NA` scalar in pandas that can be used to denote missing values.

```python
s = pd.Series([1, 2, None], dtype="Int64")
s
```
