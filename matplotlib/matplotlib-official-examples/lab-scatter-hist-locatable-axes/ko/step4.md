# 히스토그램 생성

이 단계에서는 `mpl_toolkits.axes_grid1`에서 `make_axes_locatable`을 사용하여 x 및 y 변수에 대한 히스토그램을 생성합니다.

```python
divider = make_axes_locatable(ax)
ax_histx = divider.append_axes("top", 1.2, pad=0.1, sharex=ax)
ax_histy = divider.append_axes("right", 1.2, pad=0.1, sharey=ax)

ax_histx.xaxis.set_tick_params(labelbottom=False)
ax_histy.yaxis.set_tick_params(labelleft=False)

binwidth = 0.25
xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
lim = (int(xymax/binwidth) + 1)*binwidth
bins = np.arange(-lim, lim + binwidth, binwidth)

ax_histx.hist(x, bins=bins)
ax_histy.hist(y, bins=bins, orientation='horizontal')

ax_histx.set_yticks([0, 50, 100])
ax_histy.set_xticks([0, 50, 100])
```
