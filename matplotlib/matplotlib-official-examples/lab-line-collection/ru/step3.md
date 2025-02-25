# Создаем коллекцию линий

Теперь мы можем создать объект `LineCollection` с помощью функции `LineCollection`. Мы можем задать параметры `linewidths`, `colors` и `linestyle`, чтобы настроить внешний вид линий.

```python
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

segs = np.zeros((50, 100, 2))
segs[:, :, 1] = ys
segs[:, :, 0] = x

segs = np.ma.masked_where((segs > 50) & (segs < 60), segs)

line_segments = LineCollection(segs, linewidths=(0.5, 1, 1.5, 2),
                               colors=colors, linestyle='solid')
```
