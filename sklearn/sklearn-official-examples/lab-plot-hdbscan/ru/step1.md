# Импортируем необходимые библиотеки и генерируем примерные данные

Сначала мы импортируем необходимые библиотеки и генерируем примерные данные. Мы создадим набор данных из смеси трех двухмерных и изотропных гауссовых распределений.

```python
import numpy as np
from sklearn.cluster import HDBSCAN, DBSCAN
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

centers = [[1, 1], [-1, -1], [1.5, -1.5]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=[0.4, 0.1, 0.75], random_state=0)
plt.scatter(X[:,0], X[:,1])
plt.show()
```
