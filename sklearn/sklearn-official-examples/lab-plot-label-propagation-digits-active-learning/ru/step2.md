# Перемешивание и разделение данных

Далее мы перемешаем и разделим набор данных на помеченные и не помеченные части. Начнем с только 10 помеченных точек.

```python
import numpy as np

rng = np.random.RandomState(0)
indices = np.arange(len(digits.data))
rng.shuffle(indices)

X = digits.data[indices[:330]]
y = digits.target[indices[:330]]
images = digits.images[indices[:330]]

n_total_samples = len(y)
n_labeled_points = 10
unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:]
```
