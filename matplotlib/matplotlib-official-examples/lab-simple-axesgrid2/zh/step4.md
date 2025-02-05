# 在图像网格中显示图像

最后，我们使用 `imshow` 函数和 `zip` 函数在图像网格中显示图像，以便遍历网格中的各个轴。

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
