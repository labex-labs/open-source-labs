# Graficar el límite de decisión de la longitud del camino

Al establecer `response_method="decision_function"`, el fondo de `DecisionBoundaryDisplay` representa la medida de normalidad de una observación. Tal puntuación se da por la longitud del camino promediada sobre un bosque de árboles aleatorios, que a su vez se da por la profundidad de la hoja (o equivalentemente el número de divisiones) requeridas para aislar una muestra dada.

```python
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="decision_function",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("Path length decision boundary \nof IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["outliers", "inliers"], title="true class")
plt.colorbar(disp.ax_.collections[1])
plt.show()
```
