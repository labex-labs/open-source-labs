# Ändern der Orientierung des Diagramms

In diesem Schritt ändern wir die Orientierung des Diagramms mithilfe des Parameters `orientation`. Wir setzen die Orientierung auf `'x'`, sodass die Stämme in x-Richtung projiziert werden und die Grundlinie in der yz-Ebene liegt.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
