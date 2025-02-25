# 疎と高密度の間の変換

データを疎から高密度に、またはその逆に簡単に変換できます。

```python
# 疎から高密度に変換
print(sdf.sparse.to_dense())

# 高密度から疎に変換
dense = pd.DataFrame({"A": [1, 0, 0, 1]})
dtype = pd.SparseDtype(int, fill_value=0)
print(dense.astype(dtype))
```
