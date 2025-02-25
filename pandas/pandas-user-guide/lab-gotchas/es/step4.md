# Manejo de valores NA

Pandas proporciona tipos de extensión de enteros con valores nulos para representar enteros con posibles valores faltantes.

```python
s_int = pd.Series([1, 2, 3, 4, 5], index=list("abcde"), dtype=pd.Int64Dtype())
s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
```
