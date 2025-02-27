# Генерация набора данных

Мы сгенерируем два синтетических набора данных с одинаковым математическим ожиданием, используя линейную зависимость с одной характеристикой `x`. Добавим гетероскедастический нормальный шум и асимметричный шум Партео к наборам данных.

```python
import numpy as np

rng = np.random.RandomState(42)
x = np.linspace(start=0, stop=10, num=100)
X = x[:, np.newaxis]
y_true_mean = 10 + 0.5 * x

# Гетероскедастический нормальный шум
y_normal = y_true_mean + rng.normal(loc=0, scale=0.5 + 0.5 * x, size=x.shape[0])

# Асимметричный шум Партео
a = 5
y_pareto = y_true_mean + 10 * (rng.pareto(a, size=x.shape[0]) - 1 / (a - 1))
```
