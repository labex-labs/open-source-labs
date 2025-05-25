# Lidando com Valores NA

O Pandas fornece tipos de dados de extensão de inteiro anulável (nullable-integer extension dtypes) para representar inteiros com valores possivelmente ausentes.

```python
s_int = pd.Series([1, 2, 3, 4, 5], index=list("abcde"), dtype=pd.Int64Dtype())
s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
```
