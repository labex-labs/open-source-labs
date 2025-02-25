# Составление пользовательской легенды

В этом шаге мы создадим пользовательскую легенду с использованием объектов Matplotlib. Сначала мы импортируем класс `Line2D` из модуля `matplotlib.lines`. Затем мы создаем список объектов `Line2D` с пользовательскими атрибутами цвета, ширины и метки. Наконец, мы снова строим данные с использованием функции `plot` и вызываем `legend()` с пользовательскими линиями и соответствующими метками.

```python
# Import Line2D class
from matplotlib.lines import Line2D

# Create custom lines
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Plot data and generate custom legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
