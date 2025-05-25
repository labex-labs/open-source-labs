# Plotar uma PSD básica

Primeiramente, plotaremos uma PSD básica usando dados aleatórios. Criaremos uma série temporal, adicionaremos ruído e, em seguida, plotaremos a PSD usando a função `psd` da biblioteca `matplotlib.mlab`.

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
