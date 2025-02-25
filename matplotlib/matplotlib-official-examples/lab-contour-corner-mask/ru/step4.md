# Создание графика

В этом шаге мы создадим замаскированный контурный график с использованием функции `contourf()`. Мы передаем массивы `x`, `y` и `z` в эту функцию, а также аргумент `corner_mask`, который устанавливается в `True` или `False` в зависимости от типа графика, который мы хотим создать.

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indicate masked points with red circles.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
