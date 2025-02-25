# Ajout d'axes à la figure

Nous allons ajouter des axes à la figure à l'aide de la méthode `fig.add_axes()`. Nous allons également définir la couleur d'arrière-plan des axes à l'aide de la méthode `rect.set_facecolor()`.

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
