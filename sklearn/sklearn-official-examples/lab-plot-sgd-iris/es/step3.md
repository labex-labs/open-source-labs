# Visualizar la superficie de decisión

Ahora graficaremos la superficie de decisión del modelo entrenado en el conjunto de datos iris. Usaremos la clase DecisionBoundaryDisplay para visualizar el límite de decisión del modelo.

```python
from sklearn.inspection import DecisionBoundaryDisplay

ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    xlabel=iris.feature_names[0],
    ylabel=iris.feature_names[1],
)
plt.axis("tight")
```
