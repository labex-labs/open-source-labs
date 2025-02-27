# Visualizar los resultados

Visualizaremos los resultados trazando los datos de entrenamiento, prueba y valores atípicos, junto con la frontera aprendida. También mostraremos el número de errores en los datos de prueba y los datos de valores atípicos.

```python
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Novelty Detection with LOF")
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
        "nuevas observaciones anormales",
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11),
)
plt.xlabel(
    "errores novedad regular: %d/40 ; errores novedad anormal: %d/40"
    % (n_error_test, n_error_outliers)
)
plt.show()
```
