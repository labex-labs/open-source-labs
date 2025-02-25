# テキスト用の軸の作成

このステップでは、_fig_ 内に 'matplotlib' をテキストとして含む軸を作成します。

```python
def create_text_axes(fig, height_px):
    """*fig* 内に 'matplotlib' をテキストとして含む Axes を作成します。"""
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
