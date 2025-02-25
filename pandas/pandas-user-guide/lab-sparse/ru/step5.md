# Выполнение разреженных вычислений

Мы можем применить универсальные функции NumPy к SparseArray и получить в результате SparseArray.

```python
# Creating a SparseArray
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# Applying a NumPy ufunc
print(np.abs(arr))
```
