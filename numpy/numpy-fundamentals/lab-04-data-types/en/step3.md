# Retrieving the Data Type of an Array

To determine the data type of an array, you can access the `dtype` attribute. For example:

```python
z.dtype
# returns the dtype of array z, which is uint8
```

The `dtype` object also contains information about the type, such as its bit-width and byte-order. You can use the `dtype` object to query properties of the type, such as whether it is an integer. For example:

```python
d = np.dtype(int)
# creates a dtype object for int

np.issubdtype(d, np.integer)
# returns True, indicating that d is a subdtype of np.integer

np.issubdtype(d, np.floating)
# returns False, indicating that d is not a subdtype of np.floating
```
