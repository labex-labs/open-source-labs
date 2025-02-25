# 構造化配列の比較

2つの構造化配列のdtypeが等しい場合、等号演算子 (`==`) を使って比較することができます。これにより、すべてのフィールドについて同じ値を持つ要素を示すブール型の配列が返されます。

```python
# Compare two structured arrays
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```
