# Визуализация поверхности решения

Теперь мы построим поверхность решения обученной модели на наборе данных iris. Мы будем использовать класс DecisionBoundaryDisplay для визуализации границы решения модели.

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
