# Projetez les profils de contour sur les parois du graphique

Dans cette étape, nous allons projeter les profils de contour sur les parois du graphique en traçant les contours pour chaque dimension avec des décalages appropriés.

```python
# Tracez les projections des contours pour chaque dimension
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
