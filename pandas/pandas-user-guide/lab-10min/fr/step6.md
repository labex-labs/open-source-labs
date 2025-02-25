# Opérations sur les données

Nous pouvons effectuer des opérations sur les DataFrames telles que le tri, l'application de fonctions, etc.

```python
# Tri par un axe
df.sort_index(axis=1, ascending=False)

# Application d'une fonction aux données
df.apply(np.cumsum)
```
