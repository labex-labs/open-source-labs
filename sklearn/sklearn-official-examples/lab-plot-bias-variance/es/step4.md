# Definir los modelos para comparar

Definiremos dos modelos para comparar: un solo árbol de decisión y un conjunto de bagging de árboles de decisión.

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
