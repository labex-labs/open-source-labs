# Personnalisation des graduations et des étiquettes

Nous allons personnaliser les graduations et les étiquettes des axes à l'aide de la méthode `ax1.tick_params()`. Nous allons définir la couleur, la rotation et la taille de l'étiquette de l'axe des x, et la couleur, la taille et la largeur des graduations de l'axe des y.

```python
ax1.tick_params(axis='x', labelcolor='tab:red', labelrotation=45, labelsize=16)
ax1.tick_params(axis='y', color='tab:green', size=25, width=3)
```
