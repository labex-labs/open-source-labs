# データ操作

ソートや関数の適用など、データフレームに対して操作を行うことができます。

```python
# 軸に沿ってソート
df.sort_index(axis=1, ascending=False)

# データに関数を適用
df.apply(np.cumsum)
```
