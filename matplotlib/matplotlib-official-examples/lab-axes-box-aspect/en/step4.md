# Normal Plot Next to Image

When creating an image plot with fixed data aspect and the default `adjustable="box"` next to a normal plot, the axes would be unequal in height. `set_box_aspect()` provides an easy solution to that by allowing to have the normal plot's axes use the images dimensions as box aspect. This example also shows that _constrained layout_ interplays nicely with a fixed box aspect.

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```
