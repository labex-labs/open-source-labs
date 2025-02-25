# Создаем заполненный контур с явными уровнями

Теперь мы создадим заполненный контурный график с явными уровнями. Мы будем использовать метод `contourf` с параметром `levels`, установленным на список значений, чтобы указать уровни контура. Мы также установим карту цветов на список цветов и параметр `extend` на `'both'`, чтобы показать значения за пределами диапазона уровней.

```python
# Create filled contour with explicit levels
fig, ax = plt.subplots()
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, levels, colors=('k',),
                 linewidths=(3,), origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Explicit Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')

# Show plot
plt.show()
```
