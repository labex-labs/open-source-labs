# Graficar el hiperplano de separación con el margen máximo

Finalmente, podemos graficar el hiperplano de separación con el margen máximo que obtuvimos utilizando el algoritmo de SVM con SGD. Crearemos una malla de puntos utilizando `np.meshgrid` y luego computaremos la función de decisión para cada punto de la malla utilizando el método `decision_function` del modelo de SVM. Luego graficaremos el límite de decisión utilizando `plt.contour` y los puntos de datos utilizando `plt.scatter`.

```python
# graficar la línea, los puntos y los vectores más cercanos al plano
xx = np.linspace(-1, 5, 10)
yy = np.linspace(-1, 5, 10)

X1, X2 = np.meshgrid(xx, yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function([[x1, x2]])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ["dashed", "solid", "dashed"]
colors = "k"
plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolor="black", s=20)

plt.axis("tight")
plt.show()
```
