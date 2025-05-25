# 가짜 데이터 생성

두 번째 단계에서는 차트에 사용할 가짜 데이터를 생성합니다.

```python
# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1
```
