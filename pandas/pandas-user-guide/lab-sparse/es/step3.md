# Comprendiendo SparseDtype

El `SparseDtype` almacena el tipo de datos de los valores no dispersos y el valor de relleno escalar. Lo podemos construir pasando solo un tipo de datos, o también un valor de relleno explícito.

```python
# Creando un SparseDtype
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# Creando un SparseDtype con un valor de relleno explícito
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
