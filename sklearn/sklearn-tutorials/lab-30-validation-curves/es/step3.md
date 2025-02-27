# Trazar la curva de validación

Ahora, vamos a trazar la curva de validación usando la función `validation_curve`. Usaremos el estimador `Ridge` y variaremos el hiperparámetro `alpha` en un rango de valores.

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```
