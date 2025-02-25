# Untersuchung von bestimmten Datenbereichen

Manchmal kann es erforderlich sein, bestimmte Datenbereiche in einem Bild zu untersuchen. Wir können dies tun, indem wir die Grenzen der Farbskala mit dem Parameter `clim` in der `imshow`-Funktion anpassen. Dadurch können wir uns auf bestimmte Bereiche des Bildes konzentrieren, während wir in anderen Bereichen Detailverlust hinnehmen.

```python
min_value, max_value = 100, 200
plt.imshow(img, clim=(min_value, max_value))
```
