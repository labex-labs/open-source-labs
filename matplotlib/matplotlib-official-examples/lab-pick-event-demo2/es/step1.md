# Generar datos aleatorios

Primero, necesitamos generar 100 conjuntos de datos aleatorios, cada uno contiene 1000 números aleatorios entre 0 y 1. Usaremos el módulo `random` de `numpy` para generar los datos aleatorios.

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```
