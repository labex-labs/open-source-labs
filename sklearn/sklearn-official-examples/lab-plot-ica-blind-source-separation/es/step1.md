# Generar datos de muestra

Generaremos una señal mixta de muestra que constará de tres componentes independientes. Agregaremos ruido a la señal y normalizaremos los datos. También generaremos una matriz de mezcla para mezclar nuestras tres componentes independientes.

```python
import numpy as np
from scipy import signal

np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)  # Señal 1 : señal sinusoidal
s2 = np.sign(np.sin(3 * time))  # Señal 2 : señal cuadrada
s3 = signal.sawtooth(2 * np.pi * time)  # Señal 3: señal diente de sierra

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # Agregar ruido

S /= S.std(axis=0)  # Normalizar datos
# Mezclar datos
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Matriz de mezcla
X = np.dot(S, A.T)  # Generar observaciones
```
