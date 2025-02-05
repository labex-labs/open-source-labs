# 执行图像倾斜

在这一步中，我们使用`skew_deg`函数对图像进行倾斜。我们将倾斜角度作为输入传递给`skew_deg`函数。我们使用`do_plot`函数来显示倾斜后的图像。

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
