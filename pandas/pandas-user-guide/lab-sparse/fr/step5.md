# Effectuer des calculs creux

Nous pouvons appliquer les fonctions universelles NumPy à SparseArray et obtenir un SparseArray en résultat.

```python
# Creating a SparseArray
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# Applying a NumPy ufunc
print(np.abs(arr))
```
