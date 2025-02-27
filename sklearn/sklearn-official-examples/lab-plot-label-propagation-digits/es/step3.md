# Entrenar el modelo de propagación de etiquetas

Entrenamos el modelo de propagación de etiquetas con gamma=0.25 y max_iter=20.

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```
