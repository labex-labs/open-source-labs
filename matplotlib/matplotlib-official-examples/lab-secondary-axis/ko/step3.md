# 보조 축 생성

이제 보조 축을 생성하고 x 축을 도 (degrees) 에서 라디안 (radians) 으로 변환합니다. 순방향 함수로 `deg2rad`를 사용하고 역방향 함수로 `rad2deg`를 사용합니다.

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```
