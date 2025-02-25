# Erstellen eines 3D-Konturplots

Wir werden einen 3D-Konturplot erstellen, indem wir die erstellte Triangulation und die z-Koordinaten verwenden. Wir werden auch den Blickwinkel anpassen, um den Plot besser zu verstehen.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```
