# 프로그래밍 방식으로 다각형 생성

프로그래밍 방식으로 다각형을 생성하려면 `Figure` 객체와 `Axes` 객체를 생성해야 합니다. 그런 다음 `PolygonSelector` 객체를 생성하고 정점을 추가할 수 있습니다. 마지막으로, `Axes`에 다각형을 플롯할 수 있습니다.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# Add three vertices
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
