# Conversión entre disperso y denso

Podemos convertir fácilmente los datos de disperso a denso y viceversa.

```python
# Convertir de disperso a denso
print(sdf.sparse.to_dense())

# Convertir de denso a disperso
dense = pd.DataFrame({"A": [1, 0, 0, 1]})
dtype = pd.SparseDtype(int, fill_value=0)
print(dense.astype(dtype))
```
