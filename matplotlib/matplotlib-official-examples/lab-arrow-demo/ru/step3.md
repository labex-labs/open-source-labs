# Настраиваем диаграмму с стрелками

Третий шаг - настройка диаграммы с стрелками. Мы можем изменить свойство стрелки для отображения с использованием параметра `display`. Также мы можем изменить форму стрелки с использованием параметра `shape`. Мы можем настроить ширину и расстояние между стрелками с использованием параметров `max_arrow_width` и `arrow_sep` соответственно. Мы можем изменить прозрачность стрелок с использованием параметра `alpha`. Мы также можем изменить цвет метки с использованием параметра `labelcolor`.

```python
# Plot the arrow graph with customizations
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```
