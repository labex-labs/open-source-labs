# 使用 OffsetImage 进行注释

最后，让我们使用一张格蕾丝·霍珀（Grace Hopper）的图片，通过 OffsetImage 为第二个点添加注释。

```python
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import OffsetImage

# 用一张图片（一个生成的像素数组）为第二个位置添加注释
arr = np.arange(100).reshape((10, 10))
im = OffsetImage(arr, zoom=2)
im.image.axes = ax

ab = AnnotationBbox(im, xy2,
                    xybox=(-50., 50.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.3,
                    arrowprops=dict(arrowstyle="->"))

ax.add_artist(ab)

# 用另一张图片（一张格蕾丝·霍珀的肖像）为第二个位置添加注释
with get_sample_data("grace_hopper.jpg") as file:
    arr_img = plt.imread(file)

imagebox = OffsetImage(arr_img, zoom=0.2)
imagebox.image.axes = ax

ab = AnnotationBbox(imagebox, xy2,
                    xybox=(120., -80.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.5,
                    arrowprops=dict(
                        arrowstyle="->",
                        connectionstyle="angle,angleA=0,angleB=90,rad=3")
                    )

ax.add_artist(ab)

plt.show()
```
