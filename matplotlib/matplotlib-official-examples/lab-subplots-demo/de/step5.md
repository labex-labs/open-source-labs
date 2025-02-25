# Polare Achsen

Wir können ein Gitter von polaren `Achsen` erstellen, indem wir dem Parameter `projection='polar'` der Funktion `subplots()` übergeben.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
