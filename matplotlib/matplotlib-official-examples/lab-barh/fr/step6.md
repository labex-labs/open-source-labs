# Personnaliser le graphique

Pour rendre le graphique plus informatif, nous pouvons le personnaliser en ajoutant des étiquettes, un titre et en inversant l'axe des y.

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # les étiquettes sont lues de haut en bas
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
