# Suppression d'éléments dans une liste

Vous pouvez supprimer des éléments soit par valeur d'élément, soit par index :

```python
# En utilisant la valeur
names.remove('Curtis')

# En utilisant l'index
del names[1]
```

Supprimer un élément ne crée pas de trou. Les autres éléments se déplaceront vers le haut pour combler l'espace laissé vacant. Si l'élément apparaît plus d'une fois, `remove()` ne supprimera que la première occurrence.
