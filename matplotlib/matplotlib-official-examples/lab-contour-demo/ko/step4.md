# 등고선 레이블 수동 배치

데이터 좌표에서 위치 목록을 제공하여 등고선 레이블을 수동으로 배치할 수도 있습니다.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
manual_locations = [
    (-1, -1.4), (-0.62, -0.7), (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (2.4, 1.7)]
ax.clabel(CS, inline=True, fontsize=10, manual=manual_locations)
ax.set_title('labels at selected locations')
```
