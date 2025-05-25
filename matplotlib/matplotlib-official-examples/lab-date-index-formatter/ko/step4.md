# 포맷터에 콜러블 (Callable) 사용

`.Axis.set_major_formatter`에 함수를 전달하는 대신, `__call__`을 구현하는 클래스의 인스턴스와 같은 다른 콜러블을 사용할 수 있습니다. 이 단계에서는 눈금 표시를 시간으로 형식화하는 `MyFormatter` 클래스를 생성합니다.

```python
# Use a callable for formatter
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Return the label for time x at position pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```
