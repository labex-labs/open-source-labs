# 定义一个用于标注坐标轴的函数

我们定义一个函数 `annotate_axes`，稍后将使用它为每个主要的 3D 视图平面标注其各自的角度。

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```
