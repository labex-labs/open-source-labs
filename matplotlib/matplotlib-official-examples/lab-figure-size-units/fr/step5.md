# Travail interactif rapide

Pour un travail interactif rapide, les pixels sont généralement une bonne unité de taille. Nous pouvons utiliser la valeur par défaut de dpi de 100 pour convertir les valeurs en pixels en pouces. Nous pouvons ensuite utiliser cette valeur comme paramètre figsize dans la fonction subplots. Le code ci-dessous montre comment créer une figure d'une taille de 6 pouces x 2 pouces à l'aide de valeurs en pixels.

```python
plt.subplots(figsize=(600/100, 200/100))
plt.show()
```
