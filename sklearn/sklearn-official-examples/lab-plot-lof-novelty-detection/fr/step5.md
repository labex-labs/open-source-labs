# Visualiser les résultats

Nous allons visualiser les résultats en traçant les données d'entraînement, de test et les données d'anomalies ainsi que la frontière apprise. Nous afficherons également le nombre d'erreurs dans les données de test et les données d'anomalies.

```python
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Détection de nouveauté avec LOF")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors="darkred")
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors="palevioletred")

s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c="white", s=s, edgecolors="k")
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c="blueviolet", s=s, edgecolors="k")
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c="gold", s=s, edgecolors="k")
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend(
    [a.collections[0], b1, b2, c],
    [
        "frontière apprise",
        "observations d'entraînement",
        "nouvelles observations régulières",
        "nouvelles observations anormales"
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11)
)
plt.xlabel(
    "erreurs nouvelles régulières : %d/40 ; erreurs nouvelles anormales : %d/40"
    % (n_error_test, n_error_outliers)
)
plt.show()
```
