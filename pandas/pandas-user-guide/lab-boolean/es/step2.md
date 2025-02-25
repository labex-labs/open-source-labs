# Indexación con valores NA

Pandas permite la indexación con valores `NA` en una matriz booleana, que se tratan como `False`.

```python
# Creando una Serie de pandas
s = pd.Series([1, 2, 3])

# Creando una matriz booleana con valores NA
mask = pd.array([True, False, pd.NA], dtype="boolean")

# Indexando la serie con la matriz booleana
s[mask] # Los valores NA se tratan como False
```

Si desea conservar los valores `NA`, puede rellenarlos manualmente con `fillna(True)`.

```python
# Rellenando los valores NA con True e indexando la serie
s[mask.fillna(True)]
```
