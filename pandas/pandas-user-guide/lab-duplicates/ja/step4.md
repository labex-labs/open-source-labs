# 重複ラベルの検出

`Index.is_unique` と `Index.duplicated()` メソッドを使用して、重複ラベルをチェックすることができます。

```python
# Checking if the index has unique labels
print(df1.index.is_unique)

# Checking if the columns have unique labels
print(df1.columns.is_unique)

# Detecting duplicate labels in the index
print(df1.index.duplicated())
```
