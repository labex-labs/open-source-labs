# Créez des décalages de données successifs

```python
# Simulez une série de profils de courants océaniques, successivement
# décalés de 0,1 m/s de manière à former ce qui est parfois appelé
# un graphique "en cascade" ou un graphique "étagé".

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
ax4.set_xlabel('Composante de vitesse zonale (m/s)')
ax4.set_ylabel('Profondeur (m)')
ax4.set_ylim(ax4.get_ylim()[::-1])
```

La septième étape est de créer des décalages de données successifs. Nous utiliserons la LineCollection pour créer des courbes avec des décalages successifs.
