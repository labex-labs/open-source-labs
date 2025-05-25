# 초기화 함수 정의

플롯의 초기 상태를 설정하는 초기화 함수를 정의해야 합니다. 이 함수에서 y 축 제한을 설정하고 line 객체에서 데이터를 지웁니다.

```python
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
```
