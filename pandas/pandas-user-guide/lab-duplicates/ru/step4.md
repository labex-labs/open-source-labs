# Определение дубликатов меток

Мы можем проверить наличие дубликатов меток с помощью методов `Index.is_unique` и `Index.duplicated()`.

```python
# Checking if the index has unique labels
print(df1.index.is_unique)

# Checking if the columns have unique labels
print(df1.columns.is_unique)

# Detecting duplicate labels in the index
print(df1.index.duplicated())
```
