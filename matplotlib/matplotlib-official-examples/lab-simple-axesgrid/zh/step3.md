# 遍历网格并绘制图像

然后，我们使用`zip`函数遍历`grid`对象，以便同时遍历轴和图像数组。我们使用`imshow`函数在其对应的轴上绘制每个图像。

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
