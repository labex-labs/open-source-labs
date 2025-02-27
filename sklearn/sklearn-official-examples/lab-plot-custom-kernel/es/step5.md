# Graficar el límite de decisión

En este paso, graficaremos la superficie de decisión y los vectores de soporte. Usaremos el módulo DecisionBoundaryDisplay del módulo de inspección de scikit-learn para graficar el límite de decisión. También graficaremos los puntos de entrenamiento en un diagrama de dispersión.

```python
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.title("3-Class classification using Support Vector Machine with custom kernel")
plt.axis("tight")
plt.show()
```
