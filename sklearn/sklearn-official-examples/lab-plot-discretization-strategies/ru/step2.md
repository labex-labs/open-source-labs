# Создание датасетов

Для целей визуализации мы создадим три датасета. Первый датасет будет состоять из 200 случайных выборок из равномерного распределения в обоих измерениях между -3 и 3. Второй датасет будет набором из 200 выборок, сгенерированных с использованием функции `make_blobs` из `sklearn.datasets`. Третий датасет также будет сгенерирован с использованием функции `make_blobs`.

```python
n_samples = 200
centers_0 = np.array([[0, 0], [0, 5], [2, 4], [8, 8]])
centers_1 = np.array([[0, 0], [3, 1]])

X_list = [
    np.random.RandomState(42).uniform(-3, 3, size=(n_samples, 2)),
    make_blobs(
        n_samples=[n_samples // 10, n_samples * 4 // 10, n_samples // 10, n_samples * 4 // 10],
        cluster_std=0.5,
        centers=centers_0,
        random_state=42,
    )[0],
    make_blobs(
        n_samples=[n_samples // 5, n_samples * 4 // 5],
        cluster_std=0.5,
        centers=centers_1,
        random_state=42,
    )[0],
]
```
