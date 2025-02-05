# 显示图像

使用 `imshow` 函数和不同的插值方法来显示图像。

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```
