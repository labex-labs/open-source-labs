# Treinar um Modelo de Árvore de Decisão no Conjunto de Dados Discretizado

Neste passo, treinaremos um modelo de árvore de decisão no conjunto de dados discretizado.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X_binned, y)
```
