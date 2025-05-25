# Criar MultiOutputRegressor

Criaremos um `MultiOutputRegressor` utilizando um regressor random forest como estimador subjacente. Usaremos os mesmos parâmetros da Etapa 4.

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
