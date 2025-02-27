# Генерация данных

Начнём с генерации датасета Swiss Roll с использованием функции `make_swiss_roll` из библиотеки Scikit-learn. Датасет Swiss Roll представляет собой трёхмерный датасет в виде спираль.

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# Make it thinner
X[:, 1] *= 0.5
```
