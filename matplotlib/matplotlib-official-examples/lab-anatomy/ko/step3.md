# 데이터 플롯

이제 방금 생성한 축에 데이터를 플롯합니다. `plot()` 메서드를 사용하여 세 개의 사인파를 서로 다른 색상과 선 너비로 플롯합니다.

```python
# Plot data
ax.plot(X, Y1, c='C0', lw=2.5, label="Blue signal", zorder=10)
ax.plot(X, Y2, c='C1', lw=2.5, label="Orange signal")
ax.plot(X[::3], Y3[::3], linewidth=0, markersize=9,
        marker='s', markerfacecolor='none', markeredgecolor='C4',
        markeredgewidth=2.5)
```
