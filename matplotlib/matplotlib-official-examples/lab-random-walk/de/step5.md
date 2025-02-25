# Erstellen eines 3D-Graphen

Wir erstellen einen 3D-Graphen mit `matplotlib`. Wir fügen für jeden Zufallswalk eine leere Linie zum Graphen hinzu. Wir setzen die Grenzen für die x-, y- und z-Achsen auf den Bereich zwischen 0 und 1.

```python
# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in walks]

# Setting the axes properties
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
```
