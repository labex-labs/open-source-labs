# Tracer le contour

Nous traçons le contour de la fonction de décision. Nous créons d'abord une grille de maillage à l'aide des tableaux `xx` et `yy`. Nous redimensionnons ensuite la grille de maillage en un tableau 2D et appliquons la méthode `decision_function` de la classe `SVC` pour obtenir les valeurs prédites. Nous traçons ensuite le contour à l'aide de la méthode `contourf`.

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```
