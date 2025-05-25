# UpdatingRect 클래스 생성

UpdatingRect 라는 Rectangle 의 하위 클래스를 생성합니다. 이 클래스는 Axes 인스턴스로 호출되어 사각형이 Axes 의 경계에 맞춰 모양을 업데이트하도록 합니다.

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
