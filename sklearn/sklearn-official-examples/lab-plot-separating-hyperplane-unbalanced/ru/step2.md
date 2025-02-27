# Создание данных

Мы создадим два кластера случайных точек с использованием функции `make_blobs`. Создадим один кластер из 1000 точек и другой из 100 точек. Центры кластеров будут равны `[0.0, 0.0]` и `[2.0, 2.0]` соответственно. Параметр `clusters_std` контролирует стандартное отклонение кластеров.

```python
n_samples_1 = 1000
n_samples_2 = 100
centers = [[0.0, 0.0], [2.0, 2.0]]
clusters_std = [1.5, 0.5]
X, y = make_blobs(
    n_samples=[n_samples_1, n_samples_2],
    centers=centers,
    cluster_std=clusters_std,
    random_state=0,
    shuffle=False,
)
```
