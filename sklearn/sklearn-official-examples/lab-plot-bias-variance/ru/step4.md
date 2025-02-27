# Определяем модели для сравнения

Мы определим две модели для сравнения: одно дерево решений и ансамбль деревьев решений методом bagging.

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
