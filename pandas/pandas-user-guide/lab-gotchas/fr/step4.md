# Gérer les valeurs manquantes (NA)

Pandas fournit des types d'extension de nombres entiers pouvant être nuls pour représenter des entiers avec des valeurs manquantes éventuelles.

```python
s_int = pd.Series([1, 2, 3, 4, 5], index=list("abcde"), dtype=pd.Int64Dtype())
s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
```
