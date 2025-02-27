# Построим валидационную кривую

Теперь давайте построим валидационную кривую с использованием функции `validation_curve`. Мы будем использовать оценщик `Ridge` и изменять гиперпараметр `alpha` в диапазоне значений.

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```
