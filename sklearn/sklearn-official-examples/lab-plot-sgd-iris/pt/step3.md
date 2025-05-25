# Visualizar a Superfície de Decisão

Agora, plotaremos a superfície de decisão do modelo treinado no conjunto de dados iris. Usaremos a classe `DecisionBoundaryDisplay` para visualizar a fronteira de decisão do modelo.

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
