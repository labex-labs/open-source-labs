# pcolor 플롯 생성

`ax.tricontourf`와 `fig.colorbar`를 사용하여 pcolor 플롯을 생성합니다.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tcf = ax1.tricontourf(triang, z)
fig1.colorbar(tcf)
ax1.tricontour(triang, z, colors='k')
ax1.set_title('Delaunay 삼각 분할의 등고선 플롯')
```
