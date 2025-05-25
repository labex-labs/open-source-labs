# 초기 그래프 생성

이제 사인파의 초기 그래프를 생성합니다. 진폭과 주파수에 대한 초기 매개변수를 정의하고 해당 매개변수를 사용하여 사인파를 플롯합니다.

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```
