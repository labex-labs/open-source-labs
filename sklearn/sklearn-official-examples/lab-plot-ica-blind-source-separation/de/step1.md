# Beispiel-Daten generieren

Wir werden ein Beispielgemischtes Signal generieren, das aus drei unabhängigen Komponenten besteht. Wir werden Rauschen zum Signal hinzufügen und die Daten standardisieren. Wir werden auch eine Mischmatrix generieren, um unsere drei unabhängigen Komponenten zu mischen.

```python
import numpy as np
from scipy import signal

np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)  # Signal 1 : sinusförmiges Signal
s2 = np.sign(np.sin(3 * time))  # Signal 2 : Rechtecksignal
s3 = signal.sawtooth(2 * np.pi * time)  # Signal 3: Sägezahnsignal

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # Rauschen hinzufügen

S /= S.std(axis=0)  # Daten standardisieren
# Daten mischen
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Mischmatrix
X = np.dot(S, A.T)  # Beobachtungen generieren
```
