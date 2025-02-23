# Formen zeichnen

Wir werden nun die Formen mit Matplotlib zeichnen, indem wir durch die Liste `shapes` iterieren und sie zum Plot hinzufügen.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```
