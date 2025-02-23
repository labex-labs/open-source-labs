# Создаем рисунок и настраиваем оси

Далее мы создадим рисунок и настроим оси. Мы будем использовать метод `add_axes()` для создания нового набора осей внутри рисунка. Также установим пределы для осей x и y и добавим сетку.

```python
# Create figure and axes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Set limits and gridlines
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```
