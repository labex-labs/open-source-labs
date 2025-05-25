# 플롯 방향 변경

이 단계에서는 `orientation` 매개변수를 사용하여 플롯의 방향을 변경합니다. 줄기가 x 방향으로 투영되고 기준선이 yz 평면에 있도록 방향을 `'x'`로 설정합니다.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
