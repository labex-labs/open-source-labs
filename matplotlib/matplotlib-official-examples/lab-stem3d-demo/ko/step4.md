# 플롯 사용자 정의

이 단계에서는 `bottom` 매개변수를 사용하여 기준선을 변경하고, `linefmt`, `markerfmt`, 및 `basefmt` 매개변수를 사용하여 형식을 변경하여 3D 줄기 플롯을 사용자 정의합니다.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
