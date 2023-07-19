# Understanding SparseDtype

The `SparseDtype` stores the dtype of the non-sparse values and the scalar fill value. We can construct it by passing only a dtype, or also an explicit fill value.

```python
# Creating a SparseDtype
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# Creating a SparseDtype with an explicit fill value
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
