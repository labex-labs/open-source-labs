# Rotular os Pontos Mais Incertos

Adicionaremos os rótulos humanos aos pontos de dados rotulados e treinaremos o modelo com eles.

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```
