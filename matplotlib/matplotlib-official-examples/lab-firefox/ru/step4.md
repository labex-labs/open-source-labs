# Создаем график

Теперь мы создадим график с использованием Matplotlib, добавив два объекта `PathPatch` на график. Один будет заполненной фигурой в оранжевом цвете, а другой - белым контуром.

```python
# Устанавливаем пределы графика
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# Создаем график
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # серый фон
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # центрирование
                  ylim=(ymax, ymin),  # центрирование, вверх ногами
                  xticks=[], yticks=[])  # без делений

# Добавляем белый контур
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# Добавляем оранжевую фигуру
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# Отображаем график
plt.show()
```
