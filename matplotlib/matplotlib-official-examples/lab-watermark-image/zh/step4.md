# 叠加图像

要在绘图上叠加图像，我们可以使用`matplotlib.figure.Figure`类中的`figimage`方法。我们需要指定图像、图像在绘图上的位置、z轴顺序（将图像移到前面）以及透明度（使图像半透明）。

```python
fig.figimage(im, 25, 25, zorder=3, alpha=.7)
```
