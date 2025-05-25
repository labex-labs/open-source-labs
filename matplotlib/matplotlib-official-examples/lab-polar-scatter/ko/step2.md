# 임의 데이터 생성

NumPy 를 사용하여 산점도에 대한 임의 데이터를 생성합니다. 임의의 반지름과 각도 값을 가진 150 개의 데이터 포인트를 생성하고 각 점의 면적과 색상을 계산합니다.

```python
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2
colors = theta
```
