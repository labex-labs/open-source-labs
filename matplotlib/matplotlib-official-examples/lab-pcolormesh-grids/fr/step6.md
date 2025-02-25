# Ombré automatique

Il se peut que l'utilisateur souhaite que le code choisisse automatiquement lequel utiliser. Dans ce cas, `shading='auto'` décidera d'utiliser l'ombrage `flat` ou `nearest` en fonction des formes de `X`, `Y` et `Z`. Nous pouvons visualiser la grille à l'aide du bloc de code suivant :

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='auto', cmap='viridis')
ax.set_title('Auto Shading')
plt.show()
```
