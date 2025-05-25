# Line Collection 생성

이제 `LineCollection` 함수를 사용하여 `LineCollection` 객체를 생성할 수 있습니다. 선의 모양을 사용자 정의하기 위해 `linewidths`, `colors`, 및 `linestyle` 매개변수를 설정할 수 있습니다.

```python
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

segs = np.zeros((50, 100, 2))
segs[:, :, 1] = ys
segs[:, :, 0] = x

segs = np.ma.masked_where((segs > 50) & (segs < 60), segs)

line_segments = LineCollection(segs, linewidths=(0.5, 1, 1.5, 2),
                               colors=colors, linestyle='solid')
```
