# Scope 클래스 설정

Scope 클래스는 오실로스코프를 생성하는 데 필요한 데이터와 메서드를 보유합니다. 생성자에서 필요한 변수를 초기화하고 플롯을 설정합니다.

```python
class Scope:
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)
```
