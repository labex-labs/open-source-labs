# Создание шестиугольной гистограммы

Мы создадим шестиугольную гистограмму с использованием `matplotlib.pyplot.hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

Здесь мы устанавливаем размер сетки равным 50 и карту цветов равной 'inferno'. Мы также добавляем цветовую шкалу, чтобы показать количество точек данных внутри каждого шестиугольника.
