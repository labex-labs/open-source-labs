# 초기 플롯 설정

다음으로, 초기 플롯을 설정합니다. `numpy`의 `arange` 함수를 사용하여 2 Hz 의 주파수를 가진 사인파를 생성하고, `matplotlib.pyplot`의 `plot` 함수를 사용하여 이를 플롯합니다.

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```
