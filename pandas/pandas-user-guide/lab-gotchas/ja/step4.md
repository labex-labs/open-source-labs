# NA 値の処理

Pandas は、欠損値がある可能性のある整数を表すための nullable 整数拡張型を提供しています。

```python
s_int = pd.Series([1, 2, 3, 4, 5], index=list("abcde"), dtype=pd.Int64Dtype())
s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
```
