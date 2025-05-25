# Criar um Regressor Random Forest

Criaremos um regressor random forest com uma profundidade máxima de 30 e 100 estimadores usando o `RandomForestRegressor` do scikit-learn.

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
