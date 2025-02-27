# Visualiser la surface de décision

Nous allons maintenant tracer la surface de décision du modèle entraîné sur l'ensemble de données iris. Nous utiliserons la classe DecisionBoundaryDisplay pour visualiser la frontière de décision du modèle.

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
