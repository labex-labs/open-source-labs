# 그래프 벽면에 등고선 프로파일 투영

이 단계에서는 적절한 오프셋을 사용하여 각 차원에 대한 등고선을 플롯하여 그래프 벽면에 등고선 프로파일을 투영합니다.

```python
# Plot projections of the contours for each dimension
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
