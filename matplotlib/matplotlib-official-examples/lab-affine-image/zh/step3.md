# 执行图像旋转

在这一步中，我们使用`rotate_deg`函数对图像进行旋转。我们将旋转角度作为输入传递给`rotate_deg`函数。我们使用`do_plot`函数来显示旋转后的图像。

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
