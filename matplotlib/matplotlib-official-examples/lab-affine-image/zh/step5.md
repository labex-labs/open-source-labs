# 执行图像缩放与反射

在这一步中，我们使用`scale`函数对图像进行缩放与反射操作。我们将缩放因子和反射因子作为输入传递给`scale`函数。我们使用`do_plot`函数来显示经过缩放和反射后的图像。

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1,.5))
```
