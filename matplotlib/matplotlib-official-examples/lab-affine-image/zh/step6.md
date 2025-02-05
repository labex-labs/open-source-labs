# 执行多个变换

在这一步中，我们使用`rotate_deg`、`skew_deg`、`scale`和`translate`函数对图像执行多个变换。我们将变换参数作为输入传递给相应的函数。我们使用`do_plot`函数来显示变换后的图像。

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1,.5).translate(.5, -1))
```
