# Plotar a Curva de Validação

Agora, vamos plotar a curva de validação usando a função `validation_curve`. Usaremos o estimador `Ridge` e variaremos o hiperparâmetro `alpha` em uma gama de valores.

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```
