# 타원에 대한 데이터 생성

x 좌표, y 좌표, 너비, 높이 및 각도의 배열 형태로 타원에 대한 데이터를 생성합니다.

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
