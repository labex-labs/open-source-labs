# Détection des étiquettes dupliquées

Nous pouvons vérifier s'il y a des étiquettes dupliquées en utilisant les méthodes `Index.is_unique` et `Index.duplicated()`.

```python
# Checking if the index has unique labels
print(df1.index.is_unique)

# Checking if the columns have unique labels
print(df1.columns.is_unique)

# Detecting duplicate labels in the index
print(df1.index.duplicated())
```
