# Генерация данных

Мы будем использовать функцию make_blobs из модуля sklearn.datasets для генерации синтетического набора данных с тремя кластерами. Набор данных будет состоять из 750 образцов с стандартным отклонением кластера 0,4. Мы также стандартизируем данные с использованием StandardScaler из модуля sklearn.preprocessing.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
