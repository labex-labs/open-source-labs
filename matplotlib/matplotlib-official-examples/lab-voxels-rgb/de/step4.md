# Zusammenführen der Farben

Wir werden nun die RGB-Farbbestandteile zu einem einzelnen Array der Form `(17, 17, 17, 3)` zusammenführen.

```python
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc
```
