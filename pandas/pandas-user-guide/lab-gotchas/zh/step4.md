# 处理缺失值

Pandas 提供了可空整数扩展数据类型，用于表示可能存在缺失值的整数。

```python
s_int = pd.Series([1, 2, 3, 4, 5], index=list("abcde"), dtype=pd.Int64Dtype())
s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
```
