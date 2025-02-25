# Crear una figura con dos subgráficos

Primero, necesitamos crear una figura con dos subgráficos. Usaremos el método `plt.subplots()` para crear una figura con dos subgráficos uno al lado del otro.

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```
