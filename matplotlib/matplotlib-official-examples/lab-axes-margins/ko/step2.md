# 스티키 엣지 (Sticky Edges)

Matplotlib 의 일부 플로팅 함수는 축 제한을 `margins()` 메서드에 "스티키 (sticky)"하거나 영향을 받지 않도록 합니다. 예를 들어, `imshow()` 및 `pcolor()`는 사용자가 플롯에 표시된 픽셀 주변에 제한을 좁게 설정하기를 원한다고 예상합니다. 이 동작이 원치 않는 경우, `use_sticky_edges`를 `False`로 설정해야 합니다. 이 단계에서는 Matplotlib 에서 스티키 엣지를 해결하는 방법을 배우겠습니다.

```python
# create a grid
y, x = np.mgrid[:5, 1:6]

# define polygon coordinates
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# create subplots
fig, (ax1, ax2) = plt.subplots(ncols=2)

# use sticky edges for ax1 and turn off sticky edges for ax2
ax2.use_sticky_edges = False

# plot on both subplots
for ax, status in zip((ax1, ax2), ('Is', 'Is Not')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # sticky
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # not sticky
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} Sticky')

plt.show()
```
