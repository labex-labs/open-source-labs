# 标注坐标轴

我们将使用 `text3d` 函数手动标注坐标轴。该函数接受文本的位置、要显示的文本、被视为第三维的轴以及其他参数。

```python
def text3d(ax, xyz, s, zdir="z", size=None, angle=0, usetex=False, **kwargs):
    """
    在坐标轴 *ax* 上绘制字符串 *s*，其位置为 *xyz*，大小为 *size*，
    旋转角度为 *angle*。*zdir* 给出被视为第三维的轴。*usetex* 是一个布尔值，
    指示字符串是否应通过 LaTeX 子进程运行。任何其他关键字参数
    都将转发给 `.transform_path`。

    注意：zdir 会影响对 xyz 的解释。
    """
    x, y, z = xyz
    if zdir == "y":
        xy1, z1 = (x, z), y
    elif zdir == "x":
        xy1, z1 = (y, z), x
    else:
        xy1, z1 = (x, y), z

    text_path = TextPath((0, 0), s, size=size, usetex=usetex)
    trans = Affine2D().rotate(angle).translate(xy1[0], xy1[1])

    p1 = PathPatch(trans.transform_path(text_path), **kwargs)
    ax.add_patch(p1)
    art3d.pathpatch_2d_to_3d(p1, z=z1, zdir=zdir)


text3d(ax, (4, -2, 0), "X 轴", zdir="z", size=.5, usetex=False,
       ec="none", fc="k")
text3d(ax, (12, 4, 0), "Y 轴", zdir="z", size=.5, usetex=False,
       angle=np.pi / 2, ec="none", fc="k")
text3d(ax, (12, 10, 4), "Z 轴", zdir="y", size=.5, usetex=False,
       angle=np.pi / 2, ec="none", fc="k")
```
