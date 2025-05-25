# Realizando Cálculos Esparsos

Podemos aplicar ufuncs NumPy a `SparseArray` e obter um `SparseArray` como resultado.

```python
# Creating a SparseArray
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# Applying a NumPy ufunc
print(np.abs(arr))
```
