# 데이터 정의

차트를 위한 데이터를 정의합니다. 반지름과 각도에 대한 20 개의 랜덤 값을 생성합니다.

```python
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
colors = plt.cm.viridis(radii / 10.)
```
