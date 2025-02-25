# Zeichnen des Voxel-Graphen

Schließlich können wir den Voxel-Graphen mit der Funktion `ax.voxels` zeichnen. Wir übergeben die RGB-Werte, die Bedingung für die Kugel, die Farben der Vorderflächen, die Kantenfarben und die Linienbreite.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
          edgecolors=np.clip(2*colors - 0.5, 0, 1),  # heller
          linewidth=0.5)
ax.set(xlabel='r', ylabel='g', zlabel='b')
ax.set_aspect('equal')
plt.show()
```
