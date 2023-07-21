# Create the Polygons and Add to the Plot

We create the polygons using the `PolyCollection` function from Matplotlib and add them to the plot.

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```
