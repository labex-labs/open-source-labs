# 定义渐变条形图函数

接下来，我们需要定义一个函数来创建渐变条形图。此函数将接受坐标轴对象、条形图的 x 和 y 坐标、条形图的宽度以及条形图的底部位置。然后，该函数将为每个条形图创建一个渐变图像并返回。

```python
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))
```
