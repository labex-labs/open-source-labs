# No permitir etiquetas duplicadas

Si es necesario, podemos no permitir etiquetas duplicadas utilizando el método `set_flags(allows_duplicate_labels=False)`.

```python
# No permitir etiquetas duplicadas en una Serie
try:
    pd.Series([0, 1, 2], index=["a", "b", "b"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)

# No permitir etiquetas duplicadas en un DataFrame
try:
    pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "B", "C"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)
```
