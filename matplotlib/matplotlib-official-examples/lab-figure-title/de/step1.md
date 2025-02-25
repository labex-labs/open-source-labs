# Erstellen eines gedämpften und ungedämpften Oszillationsdiagramms

Zunächst werden wir eine Grafik mit zwei Teilgrafiken erstellen, eine für eine gedämpfte Oszillation und eine für eine ungedämpfte Oszillation. Wir werden die `np.linspace()`-Funktion verwenden, um ein Array von Zeitwerten zu erstellen und dann die entsprechenden Amplitudenwerte für jede Art von Oszillation mit den `np.cos()`- und `np.exp()`-Funktionen darzustellen.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('gedämpft')
ax1.set_xlabel('Zeit (s)')
ax1.set_ylabel('Amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('Zeit (s)')
ax2.set_title('ungedämpft')

fig.suptitle('Verschiedene Arten von Oszillationen', fontsize=16)

plt.show()
```
