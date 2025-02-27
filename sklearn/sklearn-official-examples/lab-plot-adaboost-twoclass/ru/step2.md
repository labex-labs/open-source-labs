# Создаем набор данных

В этом шаге мы создадим не-линейно разделимый набор данных для классификации, состоящий из двух кластеров гауссовских квантилей, с использованием функции `make_gaussian_quantiles` из модуля `sklearn.datasets`. Также мы объединим два кластера и присвоим им метки.

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```
