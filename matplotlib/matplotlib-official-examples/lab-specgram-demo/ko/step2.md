# 신호 생성

다음으로, 플롯할 신호를 생성합니다. 이 예제에서는 서로 다른 주파수를 가진 두 개의 사인파와 약간의 무작위 노이즈의 합으로 구성된 신호를 생성합니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.0005
t = np.arange(0.0, 20.0, dt)
s1 = np.sin(2 * np.pi * 100 * t)
s2 = 2 * np.sin(2 * np.pi * 400 * t)

# create a transient "chirp"
s2[t <= 10] = s2[12 <= t] = 0

# add some noise into the mix
nse = 0.01 * np.random.random(size=len(t))

x = s1 + s2 + nse  # the signal
```
