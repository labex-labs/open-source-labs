# Генерируем случайные данные

Мы сгенерируем случайные данные с помощью функции `make_regression` из scikit-learn. Мы установим `n_samples` равным 10, `n_features` равным 10 и `random_state` равным 1. Эта функция вернет наши входные признаки X, наш целевой переменной y и истинные значения коэффициентов w.

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
