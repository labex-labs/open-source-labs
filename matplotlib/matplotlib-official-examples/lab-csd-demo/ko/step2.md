# 신호 생성

두 개의 신호를 생성해야 합니다. 이 신호들은 일관된 부분과 무작위 부분을 포함합니다. 두 신호의 일관된 부분은 10 Hz 의 주파수를 갖습니다. 신호의 무작위 부분은 저역 통과 필터를 통과하여 색상 잡음을 생성하는 백색 잡음을 사용하여 생성됩니다.

```python
dt = 0.01
t = np.arange(0, 30, dt)

# Fixing random state for reproducibility
np.random.seed(19680801)

nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt   # colored noise 1
cnse2 = np.convolve(nse2, r, mode='same') * dt   # colored noise 2

# two signals with a coherent part and a random part
s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2
```
