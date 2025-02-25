# Настройка карты цветов и параметров расширения

Наконец, мы настроим карту цветов и параметры расширения. Мы будем использовать метод `with_extremes`, чтобы установить цвета для значений ниже и выше диапазона уровней. Мы также создадим четыре подграфика, чтобы показать четыре возможных настройки `extend`: `'neither'`, `'both'`, `'min'` и `'max'`.

```python
# Set colormap and extend settings
extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

# Create subplots with different extend settings
fig, axs = plt.subplots(2, 2, layout="constrained")
for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

# Show plot
plt.show()
```
