# PathCollection 을 사용하여 히스토그램 그리기

많은 Rectangle 인스턴스를 사용하는 대신, PathCollection 을 사용하여 히스토그램을 더 빠르게 그릴 수 있습니다. 정점 (vertices) 과 코드 (codes) 를 사용하여 직접 복합 경로 (compound path) 를 생성할 것입니다. 다음 코드를 추가하십시오:

```python
nrects = len(left)
nverts = nrects*(1+3+1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom

barpath = path.Path(verts, codes)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[1].add_patch(patch)
axs[1].autoscale_view()
```
