# Projeter les profils de contour

Nous allons maintenant projeter les profils de contour sur les parois du graphique. Cela est fait en utilisant la méthode `contourf`. Nous allons définir le paramètre `zdir` sur 'z', 'x' et 'y' pour projeter respectivement les profils de contour sur les parois z, x et y. Nous allons également définir le paramètre `offset` pour correspondre aux limites d'axes appropriées.

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
