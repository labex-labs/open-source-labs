# Création d'un tracé de sinusoïde

Tout d'abord, nous devons créer un tracé de sinusoïde à l'aide des bibliothèques numpy et matplotlib.

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
```
