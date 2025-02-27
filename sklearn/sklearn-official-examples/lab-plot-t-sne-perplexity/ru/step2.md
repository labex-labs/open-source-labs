# Создаем данные

Мы создадим три различных набора данных, чтобы продемонстрировать использование t-SNE. Первый набор данных будет представлять собой две концентрические окружности.

```python
n_samples = 150
n_components = 2

X, y = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05, random_state=0
)

red = y == 0
green = y == 1
```
