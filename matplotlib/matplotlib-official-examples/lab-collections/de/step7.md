# Erstellen aufeinanderfolgender Datenverschiebungen

```python
# Simulieren einer Reihe von Ozeanstromprofilen, die sukzessive
# um 0,1 m/s versetzt werden, sodass sie das bilden, was man manchmal
# als "Wasserfall"-Diagramm oder "Stagger"-Diagramm bezeichnet.

nverts = 60
ncurves = 20
offs = (0,1, 0,0)

yy = np.linspace(0, 2*np.pi, nverts)
ym = np.max(yy)
xx = (0,2 + (ym - yy) / ym) ** 2 * np.cos(yy - 0,4) * 0,5
segs = []
for i in range(ncurves):
    xxx = xx + 0,02*rs.randn(nverts)
    curve = np.column_stack([xxx, yy * 100])
    segs.append(curve)

col = collections.LineCollection(segs, offsets=offs)
ax4.add_collection(col, autolim=True)
col.set_color(colors)
ax4.autoscale_view()

ax4.set_title('Successive data offsets')
ax4.set_xlabel('Zonal velocity component (m/s)')
ax4.set_ylabel('Depth (m)')
ax4.set_ylim(ax4.get_ylim()[::-1])
```

Als siebter Schritt werden aufeinanderfolgende Datenverschiebungen erstellt. Wir werden die LineCollection verwenden, um Kurven mit aufeinanderfolgenden Verschiebungen zu erstellen.
