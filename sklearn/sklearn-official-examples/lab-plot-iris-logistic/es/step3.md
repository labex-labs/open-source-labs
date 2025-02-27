# Mostrar los límites de decisión en el diagrama de dispersión

Mostraremos los límites de decisión en el diagrama de dispersión usando DecisionBoundaryDisplay de la biblioteca scikit-learn.

```python
_, ax = plt.subplots(figsize=(4, 3))
DecisionBoundaryDisplay.from_estimator(
    logreg,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
    xlabel="Longitud del sépalo",
    ylabel="Ancho del sépalo",
    eps=0.5,
)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors="k", cmap=plt.cm.Paired)

plt.xticks(())
plt.yticks(())

plt.show()
```
