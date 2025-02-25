# Comprendre SparseDtype

Le `SparseDtype` stocke le dtype des valeurs non creuses et la valeur de remplissage scalaire. Nous pouvons le construire en passant uniquement un dtype, ou également une valeur de remplissage explicite.

```python
# Creating a SparseDtype
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# Creating a SparseDtype with an explicit fill value
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
