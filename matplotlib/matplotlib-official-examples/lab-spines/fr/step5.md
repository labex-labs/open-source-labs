# Personnaliser les épines pour les côtés inférieur et gauche

Dans le second sous-graphique, nous allons afficher des épines uniquement sur les côtés inférieur et gauche du graphique. Nous pouvons cacher les épines sur les côtés droit et supérieur du graphique à l'aide de la méthode `set_visible`.

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```
