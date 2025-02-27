# Visualisez les résultats

Enfin, nous allons visualiser les résultats du modèle de SVM à une classe. Nous allons tracer la frontière de décision, les données d'entraînement, les observations nouvelles régulières et les observations nouvelles anormales.

```python
# Visualisez les résultats
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Détection de nouveautés")
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
    "erreur entraînement : %d/200 ; erreurs nouvelles régulières : %d/40 ; erreurs nouvelles anormales : %d/40"
    % (n_error_train, n_error_test, n_error_outliers)
)
plt.show()
```
