# Compreendendo as Diferenças com NumPy

Pandas e NumPy têm pequenas diferenças na forma como calculam a variância. Isso é importante a considerar ao alternar entre as duas bibliotecas.

```python
# Variância em pandas
var_pandas = df.var()

# Variância em NumPy
var_numpy = np.var(df.values)
```
