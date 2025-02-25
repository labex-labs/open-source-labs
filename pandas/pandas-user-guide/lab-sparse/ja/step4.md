# 疎アクセサの使用

疎データ固有の属性やメソッドを取得するには、`.sparse` アクセサを使用できます。

```python
# 疎な値を持つ Series を作成
s = pd.Series([0, 0, 1, 2], dtype="Sparse[int]")

# 疎アクセサを使用
print(s.sparse.density)
print(s.sparse.fill_value)
```
