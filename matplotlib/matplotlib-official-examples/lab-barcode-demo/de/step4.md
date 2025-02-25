# Erstellen der Figur und Achsen

Wir müssen die Figur und die Achsen für den Barcode erstellen. Wir werden die Größe der Figur auf ein Vielfaches der Anzahl der Datenpunkte setzen und alle Achsen deaktivieren.

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
```
