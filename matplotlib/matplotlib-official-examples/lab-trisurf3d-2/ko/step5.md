# 표면 플롯

마지막으로, `plot_trisurf()` 함수를 사용하여 표면을 플롯합니다. 매개변수 공간의 삼각형은 어떤 `x`, `y`, `z` 점이 모서리로 연결되는지 결정합니다.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
