# Создание простой цветовой карты

Для создания простой цветовой карты мы можем использовать класс `ListedColormap` из модуля `matplotlib.colors`. Этот класс принимает список цветов и создает из них цветовую карту.

```python
import matplotlib.colors as mcolors

# Определите список цветов
colors = ['red', 'green', 'blue']

# Создайте объект ListedColormap из списка цветов
cmap = mcolors.ListedColormap(colors)
```
