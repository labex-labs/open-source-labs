# 애니메이션 함수 정의

애니메이션 함수는 `FuncAnimation()` 함수에 의해 호출되며, 새로운 데이터로 플롯을 업데이트하는 데 사용됩니다. 이 예제에서는 시간에 따라 진폭이 변하는 사인파를 사용하여 선 그래프의 y 축 값을 업데이트합니다.

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,
```
