# Conversion d'un tableau enregistrement en tableau structuré

Pour convertir un tableau enregistrement en retournant un tableau structuré, nous pouvons utiliser la méthode `view` et spécifier le dtype d'origine du tableau structuré.

```python
# Convertit un tableau enregistrement en tableau structuré
x = recordarr.view(dtype=[('name', 'U10'), ('age', int)])
```
