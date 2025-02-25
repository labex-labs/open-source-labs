# Настраиваем метки делений на вертикальной цветовой полосе

Далее мы настроим метки делений на вертикальной цветовой полосе. Создадим цветовую полосу с использованием `colorbar` и укажем позиции делений с помощью параметра `ticks`. Затем установим метки делений с использованием `set_yticklabels` для атрибута `ax` объекта цветовой полосы.

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
