# OffsetImage で注釈を付ける

最後に、グレース・ホッパーの画像を使って OffsetImage を使って 2 番目の点に注釈を付けましょう。

```python
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import OffsetImage

# 2 番目の位置に画像 (生成されたピクセル配列) で注釈を付ける
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

# 2 番目の位置に別の画像 (グレース・ホッパーの肖像画) で注釈を付ける
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
