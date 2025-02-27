# Die Modelle definieren, die verglichen werden sollen

Wir werden zwei Modelle definieren, um sie zu vergleichen: einen einzelnen Entscheidungsbaum und ein Bagging-Ensemble von Entscheidungsbäumen.

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
