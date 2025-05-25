# 데이터 생성

등고선 플롯을 만드는 데 사용할 데이터를 생성해야 합니다. 이 예제에서는 두 개의 2D 가우시안 함수를 생성합니다.

```python
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
```
