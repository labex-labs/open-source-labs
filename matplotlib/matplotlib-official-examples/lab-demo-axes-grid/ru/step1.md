# Импортируем необходимые библиотеки и данные

Сначала нам нужно импортировать необходимые библиотеки и данные для создания нашей сетки. Мы будем использовать `matplotlib.pyplot` для построения графиков, `cbook` для получения примера набора данных и `ImageGrid` для создания нашей сетки.

```python
import matplotlib.pyplot as plt
from matplotlib import cbook
from mpl_toolkits.axes_grid1 import ImageGrid

# Получаем пример данных
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 массив
extent = (-3, 4, -4, 3)
```
