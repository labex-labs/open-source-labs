# Définissez les couleurs et créez une PatchCollection

Nous définissons les couleurs des formes et créons une `PatchCollection()`.

```python
colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)
```
