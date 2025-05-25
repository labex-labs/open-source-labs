# Prever em Novos Dados

Usaremos o regressor random forest e o regressor multi-output para fazer previsões nos nossos dados de teste.

```python
y_rf = regr_rf.predict(X_test)
y_multirf = regr_multirf.predict(X_test)
```
