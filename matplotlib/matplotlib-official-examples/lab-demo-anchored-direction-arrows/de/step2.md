# Erstellen eines Graphen

Als nächstes werden wir einen einfachen Graphen mit NumPy erstellen. Dieser Graphen wird als Hintergrund für die ankergestützten Richtungsarrows dienen.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
