# Создание набора данных Swiss Roll

Начнем с создания набора данных Swiss Roll с использованием функции `make_swiss_roll()` из `sklearn.datasets`. Эта функция создает трехмерный набор данных в виде спиральной формы.

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```
