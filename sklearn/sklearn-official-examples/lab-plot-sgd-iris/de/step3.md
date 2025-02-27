# Entscheidungsfläche visualisieren

Wir werden nun die Entscheidungsfläche des trainierten Modells auf dem Iris-Datensatz darstellen. Wir werden die DecisionBoundaryDisplay-Klasse verwenden, um die Entscheidungsgrenze des Modells zu visualisieren.

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
