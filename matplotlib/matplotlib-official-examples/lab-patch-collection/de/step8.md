# Farben festlegen und PatchCollection erstellen

Wir legen die Farben der Formen fest und erstellen eine `PatchCollection()`.

```python
colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
p.set_array(colors)
ax.add_collection(p)
fig.colorbar(p, ax=ax)
```
