# Conversion entre les formats creux et dense

Nous pouvons facilement convertir les données du format creux au format dense, et vice versa.

```python
# Converting from sparse to dense
print(sdf.sparse.to_dense())

# Converting from dense to sparse
dense = pd.DataFrame({"A": [1, 0, 0, 1]})
dtype = pd.SparseDtype(int, fill_value=0)
print(dense.astype(dtype))
```
