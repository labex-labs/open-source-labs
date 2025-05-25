# 극좌표 그래프 생성

다음으로, figure 를 정의하고 극좌표 투영 (polar projection) 을 갖도록 지정하여 극좌표 그래프를 생성합니다. 또한 플로팅에 사용할 반경 (radius) 및 세타 (theta) 값을 정의합니다.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)
```
