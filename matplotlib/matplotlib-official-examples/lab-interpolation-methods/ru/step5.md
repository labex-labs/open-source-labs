# Отобразить изображения

Отобразите изображения с использованием функции `imshow` и различных методов интерполяции.

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```
