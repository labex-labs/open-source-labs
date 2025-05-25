# Comparando Arrays Estruturados

Se os dtypes de dois arrays estruturados forem iguais, podemos compará-los usando o operador de igualdade (`==`). Isso retornará um array booleano indicando quais elementos possuem os mesmos valores para todos os campos.

```python
# Compare two structured arrays
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```
