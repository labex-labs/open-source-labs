# 임의 데이터 생성

NumPy 의 `np.random.uniform` 메서드를 사용하여 임의 데이터를 생성합니다. -2 와 2 사이의 x 및 y 값을 갖는 `npts = 200`개의 데이터 포인트를 생성합니다. 또한 함수 `z = x * np.exp(-x**2 - y**2)`를 사용하여 z 값을 계산합니다.

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```
