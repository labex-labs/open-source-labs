# Graficar el hiperplano separador de márgen máximo

Para graficar el hiperplano separador de márgen máximo, usaremos la función `DecisionBoundaryDisplay.from_estimator()` de scikit-learn. Esta función grafica la función de decisión y los vectores de soporte del clasificador de SVM. También graficaremos los vectores de soporte como círculos sin relleno y con un borde negro.

```python
from sklearn.inspection import DecisionBoundaryDisplay

# plot the decision function and support vectors
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
```
