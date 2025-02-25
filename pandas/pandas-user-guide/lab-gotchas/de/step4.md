# Das Umgang mit NA-Werten

Pandas bietet nullable-integer-Erweiterungsdatentypen an, um ganze Zahlen mit möglicherweise fehlenden Werten zu repräsentieren.

```python
s_int = pd.Series([1, 2, 3, 4, 5], index=list("abcde"), dtype=pd.Int64Dtype())
s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
```
