# Создание пользовательских цветовых карты

Matplotlib также позволяет создавать пользовательские цветовые карты. Это может быть полезно, когда встроенные цветовые карты не обеспечивают нужного представления данных.

```python
import matplotlib.colors as mcolors

# Определите список цветов и их соответствующих значений
colors = [(0,'red'), (0.5, 'green'), (1, 'blue')]

# Создайте объект LinearSegmentedColormap из списка цветов
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', colors)
```
