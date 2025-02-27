# Генерация выборочных данных

Мы генерируем выборочные данные с использованием функции `make_checkerboard`. Каждый пиксель в `shape=(300, 300)` представляет собой значение из равномерного распределения с помощью своего цвета. Шум добавляется из нормального распределения, где значение, выбранное для `noise`, является стандартным отклонением.

```python
from sklearn.datasets import make_checkerboard
from matplotlib import pyplot as plt

n_clusters = (4, 3)
data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10, shuffle=False, random_state=42
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
_ = plt.show()
```
