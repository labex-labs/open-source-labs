# Аннотация с использованием OffsetImage

Наконец, давайте добавим аннотацию ко второй точке с использованием OffsetImage и изображением Греис Хоппер.

```python
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import OffsetImage

# Добавим аннотацию ко второй позиции с использованием изображения (сгенерированного массива пикселей)
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

# Добавим аннотацию ко второй позиции с использованием другого изображения (портрета Греис Хоппер)
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
