# Verwenden des spärren Zugriffsmethoden

Wir können den `.sparse`-Zugriff verwenden, um Attribute und Methoden für spärre Daten zu erhalten.

```python
# Creating a Series with sparse values
s = pd.Series([0, 0, 1, 2], dtype="Sparse[int]")

# Using the sparse accessor
print(s.sparse.density)
print(s.sparse.fill_value)
```
