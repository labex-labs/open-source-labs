# Treinar um Modelo de Árvore de Decisão

Neste passo, treinaremos um modelo de árvore de decisão no conjunto de dados original.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
