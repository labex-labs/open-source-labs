# Trazar el límite de decisión del modelo de regresión logística multinomial

Ahora trazaremos la superficie de decisión del modelo de regresión logística multinomial usando la función `DecisionBoundaryDisplay` de scikit-learn. Estableceremos el método de respuesta en `"predict"`, la mapa de colores en `"plt.cm.Paired"` y también graficaremos los puntos de entrenamiento.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("Decision surface of LogisticRegression (multinomial)")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
