# 변수 설정

다음으로, 신호에 대한 변수를 설정합니다. 샘플링 간격은 0.01 로 설정하며, 이는 100 Hz 의 샘플링 주파수를 제공합니다. 0 초에서 10 초까지 0.01 초 간격으로 시간 배열을 생성합니다. 또한 NumPy 의 `randn` 함수를 사용하여 노이즈를 생성하고, 지수 감쇠 함수와 컨볼루션 (convolve) 하여 노이즈가 있는 신호를 생성합니다.

```python
np.random.seed(0)

dt = 0.01  # sampling interval
Fs = 1 / dt  # sampling frequency
t = np.arange(0, 10, dt)

# generate noise:
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s = 0.1 * np.sin(4 * np.pi * t) + cnse  # the signal
```
