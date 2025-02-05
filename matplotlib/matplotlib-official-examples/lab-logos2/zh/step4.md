# 创建文本轴

在这一步中，我们将在 _fig_ 中创建一个轴，其中包含文本“matplotlib”。

```python
def create_text_axes(fig, height_px):
    """在 *fig* 中创建一个包含文本“matplotlib”的轴。"""
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_aspect("equal")
    ax.set_axis_off()

    path = TextPath((0, 0), "matplotlib", size=height_px * 0.8,
                    prop=get_font_properties())

    angle = 4.25  # 度
    trans = mtrans.Affine2D().skew_deg(angle, 0)

    patch = PathPatch(path, transform=trans + ax.transData, color=MPL_BLUE,
                      lw=0)
    ax.add_patch(patch)
    ax.autoscale()
```
