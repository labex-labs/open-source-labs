# Durchführen von spärren Berechnungen

Wir können NumPy ufuncs auf SparseArray anwenden und als Ergebnis ein SparseArray erhalten.

```python
# Creating a SparseArray
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# Applying a NumPy ufunc
print(np.abs(arr))
```
