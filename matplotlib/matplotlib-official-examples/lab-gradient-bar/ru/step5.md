# Создаем график

Теперь мы можем создать график. Сначала мы создадим фигуру и объект оси. Затем мы установим пределы по осям x и y. Мы создадим градиентный фон с использованием функции `gradient_image()`. Наконец, мы создадим случайный набор данных и используем функцию `gradient_bar()` для создания столбчатой диаграммы.

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# background image
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
