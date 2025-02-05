# Generate the Path object and make a patch out of it

Next, we will generate a Path object and make a patch out of it. We will use the Path object to draw our histogram using rectangles. Add the following code:

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
