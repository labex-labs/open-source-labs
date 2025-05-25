# 제한 설정 및 그리드 표시

이 단계에서는 축의 제한을 설정하고 그리드를 표시합니다. `set_aspect()`를 사용하여 축의 종횡비를 설정하고 `grid()`를 사용하여 그리드를 표시합니다.

```python
# Set the limits and display the grid
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
