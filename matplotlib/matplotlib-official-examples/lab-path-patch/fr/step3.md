# Créer un objet PathPatch

Dans cette étape, nous créons un objet `PathPatch` à l'aide de l'objet de tracé que nous avons créé dans l'étape précédente. Cet objet est utilisé pour remplir la zone entourée par le tracé. Nous pouvons également définir la couleur et la transparence du patch.

```python
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
```
