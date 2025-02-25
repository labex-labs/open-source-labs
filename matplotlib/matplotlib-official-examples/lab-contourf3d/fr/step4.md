# Créez le tracé de contour

Nous allons maintenant créer le tracé de contour en utilisant la méthode `contourf()`. Cette méthode crée des contours remplis. Nous définirons le paramètre `cmap` sur `cm.coolwarm` pour utiliser la carte de couleurs froid-chaud.

```python
ax.contourf(X, Y, Z, cmap=cm.coolwarm)
```
