# 초기 조건 설정 및 ODE (상미분 방정식) 적분

이제 시뮬레이션을 위한 초기 조건을 설정합니다. 각 진자의 초기 각도와 각속도, 그리고 시뮬레이션의 시간 간격을 설정합니다. 그런 다음 오일러 방법 (Euler's method) 을 사용하여 ODE 를 적분하여 각 시간 단계에서 각 진자의 위치와 속도를 구합니다.

```python
# 0..t_stop 에서 0.02 초 간격으로 샘플링된 시간 배열 생성
dt = 0.01
t = np.arange(0, t_stop, dt)

# th1 과 th2 는 초기 각도 (도)
# w10 과 w20 은 초기 각속도 (초당 도)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# 초기 상태
state = np.radians([th1, w1, th2, w2])

# 오일러 방법을 사용하여 ODE 적분
y = np.empty((len(t), 4))
y[0] = state
for i in range(1, len(t)):
    y[i] = y[i - 1] + derivs(t[i - 1], y[i - 1]) * dt
```
