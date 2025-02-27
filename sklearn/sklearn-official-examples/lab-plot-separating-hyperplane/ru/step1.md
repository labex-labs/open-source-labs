# Создание двухклассового разделимого набора данных

Для создания двухклассового разделимого набора данных мы будем использовать функцию `make_blobs()` из scikit-learn. Эта функция генерирует изотропные гауссовы "куски" для кластеризации и классификации. Мы создадим 40 образцов с двумя центрами и случайным种子ом 6. Также мы построим точки данных с использованием `matplotlib`.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# create a two-class separable dataset
X, y = make_blobs(n_samples=40, centers=2, random_state=6)

# plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()
```
