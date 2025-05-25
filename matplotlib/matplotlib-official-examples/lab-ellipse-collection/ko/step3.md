# Ellipse Collection 생성

위의 데이터를 사용하여 `EllipseCollection`을 생성하고, 단위를 'x'로, 오프셋을 `XY`로 지정합니다.

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
