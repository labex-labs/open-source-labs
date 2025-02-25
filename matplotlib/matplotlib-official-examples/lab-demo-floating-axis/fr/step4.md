# Créer les axes hôtes

Dans cette étape, nous allons créer les axes hôtes et définir l'aide à la grille. Nous utiliserons `fig.add_subplot()` pour créer les axes hôtes.

```python
# Créer les axes hôtes
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```
