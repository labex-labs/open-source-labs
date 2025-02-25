# 画像を表示する

`imshow`関数とさまざまな補間方法を使って画像を表示します。

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```
