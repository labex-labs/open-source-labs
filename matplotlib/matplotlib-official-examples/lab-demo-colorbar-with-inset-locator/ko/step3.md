# Inset Axes 를 사용하여 컬러바 추가

이제 inset_axes 를 사용하여 각 이미지에 컬러바를 추가합니다. 첫 번째 컬러바는 ax1 에, 두 번째는 ax2 에 추가됩니다.

```python
# add colorbar to ax1
axins1 = inset_axes(
    ax1,
    width="50%",  # width: parent_bbox 너비의 50%
    height="5%",  # height: 5%
    loc="upper right",
)
axins1.xaxis.set_ticks_position("bottom")
fig.colorbar(im1, cax=axins1, orientation="horizontal", ticks=[1, 2, 3])

# add colorbar to ax2
axins2 = inset_axes(
    ax2,
    width="5%",  # width: parent_bbox 너비의 5%
    height="50%",  # height: 50%
    loc="lower left",
    bbox_to_anchor=(1.05, 0., 1, 1),
    bbox_transform=ax2.transAxes,
    borderpad=0,
)
fig.colorbar(im2, cax=axins2, ticks=[1, 2, 3])
```
