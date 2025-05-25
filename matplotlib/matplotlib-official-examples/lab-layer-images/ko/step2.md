# x 및 y 변수 정의

meshgrid 를 생성하기 위해 x 및 y 변수를 정의합니다.

```python
dx, dy = 0.05, 0.05
x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)
```
