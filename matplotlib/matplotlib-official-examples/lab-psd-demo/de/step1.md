# Ein einfaches Leistungsdichtespektrum (PSD) darstellen

Zunächst werden wir ein einfaches PSD mit zufälligen Daten darstellen. Wir werden eine Zeitreihe erstellen, Rauschen hinzufügen und dann das PSD mit der `psd`-Funktion aus der `matplotlib.mlab`-Bibliothek darstellen.

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
