# Personnalisez le tracé

Pour personnaliser le tracé, nous pouvons utiliser les méthodes suivantes :

- `set_rmax` pour définir la valeur maximale de `r`
- `set_rticks` pour définir les valeurs d'échelonnage de `r`
- `set_rlabel_position` pour définir la position des étiquettes radiales

```python
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
```

Nous pouvons également ajouter un titre au tracé en utilisant la méthode `set_title`.

```python
ax.set_title("A line plot on a polar axis", va='bottom')
```

Enfin, nous pouvons ajouter une grille au tracé en utilisant la méthode `grid`.

```python
ax.grid(True)
```
