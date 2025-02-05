# Change the orientation of the plot

In this step, we will change the orientation of the plot using the `orientation` parameter. We will set the orientation to `'x'` so that the stems are projected along the x-direction and the baseline is in the yz-plane.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
