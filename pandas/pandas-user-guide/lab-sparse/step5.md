# Performing Sparse Calculations

We can apply NumPy ufuncs to SparseArray and get a SparseArray as a result.

```python
# Creating a SparseArray
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# Applying a NumPy ufunc
print(np.abs(arr))
```
