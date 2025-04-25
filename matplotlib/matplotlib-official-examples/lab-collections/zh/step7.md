# 创建连续的数据偏移量

```python
# 依次模拟一系列海洋流剖面，
# 每次偏移 0.1 米/秒，以便它们形成有时被称为
# “瀑布”图或“交错”图的图形。

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

第七步是创建连续的数据偏移量。我们将使用 LineCollection 来创建具有连续偏移量的曲线。
