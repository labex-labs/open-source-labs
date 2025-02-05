# Create 3D contour plot

We will create a 3D contour plot using the created triangulation and the z coordinates. We will also customize the view angle so it's easier to understand the plot.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```
