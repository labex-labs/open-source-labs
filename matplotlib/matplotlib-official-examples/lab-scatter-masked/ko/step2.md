# 산점도 데이터 생성

다음으로, 산점도에 대한 데이터를 생성합니다. 0 과 0.9 사이의 임의의 x 및 y 값과 0 과 10 사이의 임의의 반지름을 가진 100 개의 데이터 포인트를 생성합니다. 각 데이터 포인트의 색상은 해당 영역의 제곱근에 의해 결정됩니다.

```python
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
```
