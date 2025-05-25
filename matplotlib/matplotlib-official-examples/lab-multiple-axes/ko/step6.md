# 애니메이션 함수 정의

여섯 번째 단계는 애니메이션 함수를 정의하는 것입니다. 이 함수는 애니메이션의 각 프레임마다 호출되며, 왼쪽 subplot 의 점 위치, 오른쪽 subplot 의 사인 곡선의 위치 및 데이터, 그리고 연결 패치의 위치를 업데이트합니다.

```python
def animate(i):
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    x, y = np.cos(i), np.sin(i)
    point.set_data([x], [y])
    con.xy1 = x, y
    con.xy2 = i, y
    return point, sine, con
```
