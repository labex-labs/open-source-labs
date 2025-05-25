# x, y, z 값 정의

NumPy 를 사용하여 x, y, z 의 값을 생성합니다. 먼저 theta 와 z 의 값 범위를 정의합니다. 그런 다음, 이 값들을 사용하여 r, x, y 의 값을 생성합니다.

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
