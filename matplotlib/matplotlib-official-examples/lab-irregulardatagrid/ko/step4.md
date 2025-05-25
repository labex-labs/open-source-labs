# Tricontour

`axes.Axes.tricontour`에 정렬되지 않은 불규칙하게 배치된 좌표를 직접 제공하여 동일한 데이터를 tricontour 플롯으로 플롯합니다.

```python
fig, ax2 = plt.subplots()
cntr2 = ax2.tricontourf(x, y, z, levels=14, cmap="RdBu_r")
ax2.plot(x, y, 'ko', ms=3)
ax2.set(xlim=(-2, 2), ylim=(-2, 2))
ax2.set_title('Tricontour Plot of Irregularly Spaced Data')
fig.colorbar(cntr2, ax=ax2)
plt.show()
```
