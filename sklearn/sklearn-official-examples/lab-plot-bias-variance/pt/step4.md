# Definir os Modelos para Comparação

Vamos definir dois modelos para comparação: uma única árvore de decisão e um conjunto de árvores de decisão por _bagging_.

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
