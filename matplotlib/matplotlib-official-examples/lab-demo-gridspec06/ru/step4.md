# Создание внутренних сеток и подграфиков

В этом шаге мы создадим внутренние сетки и подграфики с использованием вложенных `.GridSpec`. Мы пройдемся по каждой ячейке в внешней сетке и создадим для каждой ячейки 3x3 сетку.

```python
for a in range(4):
    for b in range(4):
        # gridspec внутри gridspec
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots()  # Создаем все подграфики для внутренней сетки.
        for (c, d), ax in np.ndenumerate(axs):
            ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
            ax.set(xticks=[], yticks=[])
```
