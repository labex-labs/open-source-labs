# Déplacer les étiquettes des graduations de l'axe des x en haut

Pour déplacer les étiquettes des graduations de l'axe des x en haut, nous allons utiliser la fonction `tick_params()` et définir les paramètres `top` et `labeltop` sur `True`, et les paramètres `bottom` et `labelbottom` sur `False`.

```python
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
```
