# Kreise erstellen

Wir erstellen Kreise mit `Circle()` und fügen sie einer Liste von Patches hinzu.

```python
x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1*np.random.rand(N)
patches = []
for x1, y1, r in zip(x, y, radii):
    circle = Circle((x1, y1), r)
    patches.append(circle)
```
