# Den Plot erstellen

Jetzt werden wir den Plot mit der Funktion `tricontourf()` erstellen und den Blickwinkel anpassen.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```
