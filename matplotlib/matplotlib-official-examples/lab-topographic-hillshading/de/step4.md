# Festlegen der Lichtquelle und der Farbskala

Wir legen das LightSource-Objekt fest, indem wir die Azimut- und Höhenwinkel der Lichtquelle festlegen. Wir legen auch die Farbskala fest, die im Diagramm verwendet werden soll.

```python
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
```
