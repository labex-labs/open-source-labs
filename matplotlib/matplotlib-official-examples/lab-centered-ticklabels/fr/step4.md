# Supprimer les étiquettes des graduations majeures et les graduations mineures

Pour simuler le comportement de centrage des étiquettes entre les graduations, nous devons supprimer les étiquettes des graduations majeures et les graduations mineures et ne montrer que les étiquettes des graduations mineures. Nous pouvons le faire à l'aide de la fonction `tick_params()` et en définissant les paramètres `tick1On` et `tick2On` sur `False`.

```python
# Supprimer les lignes de graduation
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
```
