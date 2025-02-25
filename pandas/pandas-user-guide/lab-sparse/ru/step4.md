# Использование разреженного доступатора

Мы можем использовать доступатор `.sparse`, чтобы получить атрибуты и методы, специфичные для разреженных данных.

```python
# Creating a Series with sparse values
s = pd.Series([0, 0, 1, 2], dtype="Sparse[int]")

# Using the sparse accessor
print(s.sparse.density)
print(s.sparse.fill_value)
```
