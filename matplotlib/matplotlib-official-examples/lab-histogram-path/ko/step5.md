# Path 객체 생성 및 패치 (patch) 만들기

다음으로, Path 객체를 생성하고 이를 기반으로 패치를 만들 것입니다. 사각형을 사용하여 히스토그램을 그리기 위해 Path 객체를 사용할 것입니다. 다음 코드를 추가하십시오:

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
