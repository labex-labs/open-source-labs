# 범례가 있는 색상 없는 해치 플롯

이 단계에서는 색상이 없는 해치 플롯을 생성하고 범례를 추가합니다. `contour` 함수를 사용하여 등고선 (contour lines) 을 생성하고, `contourf` 함수를 사용하여 색상 없이 해치를 지정합니다.

```python
fig2, ax2 = plt.subplots()
n_levels = 6
ax2.contour(x, y, z, n_levels, colors='black', linestyles='-')
cs = ax2.contourf(x, y, z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')

# create a legend for the contour set
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax2.legend(artists, labels, handleheight=2, framealpha=1)
```
