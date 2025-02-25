# Das Erkennen von doppelten Labels

Wir können nach doppelten Labels mithilfe der Methoden `Index.is_unique` und `Index.duplicated()` prüfen.

```python
# Checking if the index has unique labels
print(df1.index.is_unique)

# Checking if the columns have unique labels
print(df1.columns.is_unique)

# Detecting duplicate labels in the index
print(df1.index.duplicated())
```
