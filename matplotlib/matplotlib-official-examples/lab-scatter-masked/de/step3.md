# Maskieren von Datenpunkten und Erstellen eines Streudiagramms

Wir maskieren die Datenpunkte basierend auf ihrem Abstand vom Ursprung. Datenpunkte mit einem Abstand kleiner als `r0` werden in `area1` maskiert, und diejenigen mit einem Abstand größer oder gleich `r0` werden in `area2` maskiert. Anschließend erstellen wir ein Streudiagramm der maskierten Datenpunkte mit `marker='^'` und `marker='o'` für `area1` und `area2` respective.

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```
