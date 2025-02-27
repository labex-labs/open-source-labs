# Visualizar los resultados

Finalmente, visualizaremos los resultados del modelo de one-class SVM. Graficaremos el límite de decisión, los datos de entrenamiento, las observaciones novedosas regulares y las observaciones novedosas anormales.

```python
# Visualize the results
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Novelty Detection")
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
        "frontier aprendida",
        "observaciones de entrenamiento",
        "nuevas observaciones regulares",
        "nuevas observaciones anormales"
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11)
)
plt.xlabel(
    "error train: %d/200 ; errores novedades regulares: %d/40 ; errores novedades anormales: %d/40"
    % (n_error_train, n_error_test, n_error_outliers)
)
plt.show()
```
