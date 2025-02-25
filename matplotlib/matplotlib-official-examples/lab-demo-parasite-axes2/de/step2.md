# Host- und Parasitenachsen erstellen

Wir werden eine Host-Achse und zwei Parasitenachsen mit den Funktionen `host_subplot()` und `twinx()` erstellen. Die `host_subplot()`-Funktion erstellt eine Host-Achse, und die `twinx()`-Funktion erstellt Parasitenachsen, die die gleiche x-Achse mit der Host-Achse teilen.

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
