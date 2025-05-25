# Treinar o Modelo de Propagação de Rótulos

Treinamos o modelo de Propagação de Rótulos com gamma=0.25 e max_iter=20.

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```
