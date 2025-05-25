# 플롯에 오차 막대 추가

`Axes3D` 객체의 `errorbar` 메서드를 사용하여 플롯에 오차 막대를 추가합니다. `zuplims` 및 `zlolims` 매개변수를 상한 및 하한을 갖는 데이터 포인트를 지정하는 배열로 설정합니다. `errorevery` 매개변수를 설정하여 오차 막대의 빈도를 제어합니다.

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```
