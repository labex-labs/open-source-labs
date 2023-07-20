# Set colors and create PatchCollection

We set the colors of the shapes and create a `PatchCollection()`.

```python
colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)
```
