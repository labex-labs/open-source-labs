# 해칭된 등고선 플롯 생성

`ax.tricontourf`에서 `hatches` 매개변수를 지정하여 해칭된 등고선 플롯을 생성할 수 있습니다. 또한 `cmap` 매개변수를 지정하여 다른 컬러맵 (colormap) 을 사용할 수도 있습니다.

```python
fig2, ax2 = plt.subplots()
ax2.set_aspect("equal")
tcf = ax2.tricontourf(
    triang,
    z,
    hatches=["*", "-", "/", "//", "\\", None],
    cmap="cividis"
)
fig2.colorbar(tcf)
ax2.tricontour(triang, z, linestyles="solid", colors="k", linewidths=2.0)
ax2.set_title("Delaunay 삼각 분할의 해칭된 등고선 플롯")
```
