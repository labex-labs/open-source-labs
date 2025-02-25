# Utilisation de l'accesseur creux

Nous pouvons utiliser l'accesseur `.sparse` pour obtenir des attributs et des méthodes spécifiques aux données creuses.

```python
# Creating a Series with sparse values
s = pd.Series([0, 0, 1, 2], dtype="Sparse[int]")

# Using the sparse accessor
print(s.sparse.density)
print(s.sparse.fill_value)
```
