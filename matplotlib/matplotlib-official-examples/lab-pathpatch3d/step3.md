# Draw a Circle on the Wall

We will draw a circle on the x=0 'wall' of the 3D plot using the `Circle` and `pathpatch_2d_to_3d` functions of Matplotlib.

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```
