# 플롯 생성

이 단계에서는 `contourf()` 함수를 사용하여 마스크된 등고선 플롯을 생성합니다. `x`, `y`, `z` 배열과 함께, 생성하려는 플롯 유형에 따라 `corner_mask` 인수를 `True` 또는 `False`로 설정하여 이 함수에 전달합니다.

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indicate masked points with red circles.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
