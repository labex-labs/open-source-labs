# 生成路径对象并从中创建一个补丁

接下来，我们将生成一个路径对象并从中创建一个补丁。我们将使用该路径对象通过矩形来绘制我们的直方图。添加以下代码：

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
