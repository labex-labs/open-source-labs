# 클래스 정의

데이터를 다운샘플링하고 확대/축소 시 다시 계산하는 `DataDisplayDownsampler` 클래스를 정의합니다. 클래스의 생성자는 xdata 와 ydata 를 입력 매개변수로 사용합니다. 최대 점 수를 50 으로 설정하고 xdata 의 델타를 계산합니다.

```python
class DataDisplayDownsampler:
    def __init__(self, xdata, ydata):
        self.origYData = ydata
        self.origXData = xdata
        self.max_points = 50
        self.delta = xdata[-1] - xdata[0]
```
