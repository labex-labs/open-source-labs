# Realizando cálculos dispersos

Podemos aplicar funciones universales (ufuncs) de NumPy a SparseArray y obtener un SparseArray como resultado.

```python
# Creando un SparseArray
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# Aplicando una función universal de NumPy
print(np.abs(arr))
```
