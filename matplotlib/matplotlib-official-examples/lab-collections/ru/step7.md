# Создать последовательные смещения данных

```python
# Симулировать серию профилей океанических течений,
# последовательно смещенных на 0,1 м/с, чтобы они образовывали то,
# что иногда называют "водопадной" диаграммой или "стаканчиковой" диаграммой.

nverts = 60
ncurves = 20
offs = (0.1, 0.0)

yy = np.linspace(0, 2*np.pi, nverts)
ym = np.max(yy)
xx = (0.2 + (ym - yy) / ym) ** 2 * np.cos(yy - 0.4) * 0.5
segs = []
for i in range(ncurves):
    xxx = xx + 0.02*rs.randn(nverts)
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

Седьмым шагом является создание последовательных смещений данных. Мы будем использовать LineCollection для создания кривых с последовательными смещениями.
