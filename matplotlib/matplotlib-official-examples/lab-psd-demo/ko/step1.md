# 기본 PSD 플롯

먼저, 임의의 데이터를 사용하여 기본 PSD 를 플롯합니다. 시계열을 생성하고, 노이즈를 추가한 다음, `matplotlib.mlab` 라이브러리의 `psd` 함수를 사용하여 PSD 를 플롯합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

np.random.seed(19680801)
dt = 0.01
t = np.arange(0, 10, dt)
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]
s = 0.1 * np.sin(2 * np.pi * t) + cnse

fig, (ax0, ax1) = plt.subplots(2, 1)
ax0.plot(t, s)
ax1.psd(s, 512, 1 / dt)

plt.show()
```
