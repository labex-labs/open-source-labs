# Delaunay 삼각 측량 플롯

`triplot` 함수를 사용하여 삼각 측량 (triangulation) 을 플롯합니다.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'bo-', lw=1)
ax1.set_title('Delaunay Triangulation 의 Triplot')
```
