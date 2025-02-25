# Добавляем цветовую полосу с использованием вставленных осей

Теперь мы добавим цветовую полосу к каждому изображению с использованием inset_axes. Первая цветовая полоса будет добавлена к ax1, а вторая - к ax2.

```python
# add colorbar to ax1
axins1 = inset_axes(
    ax1,
    width="50%",  # width: 50% of parent_bbox width
    height="5%",  # height: 5%
    loc="upper right",
)
axins1.xaxis.set_ticks_position("bottom")
fig.colorbar(im1, cax=axins1, orientation="horizontal", ticks=[1, 2, 3])

# add colorbar to ax2
axins2 = inset_axes(
    ax2,
    width="5%",  # width: 5% of parent_bbox width
    height="50%",  # height: 50%
    loc="lower left",
    bbox_to_anchor=(1.05, 0., 1, 1),
    bbox_transform=ax2.transAxes,
    borderpad=0,
)
fig.colorbar(im2, cax=axins2, ticks=[1, 2, 3])
```
