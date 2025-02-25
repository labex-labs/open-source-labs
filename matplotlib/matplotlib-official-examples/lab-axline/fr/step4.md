# Tracer des lignes diagonales

Nous pouvons utiliser `axline` avec le paramètre `transform` pour tracer des lignes diagonales avec une pente fixe. Traçons des lignes de grille diagonales avec une pente fixe de `0,5`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Tracer des lignes diagonales
for pos in np.linspace(-2, 1, 10):
    plt.axline((pos, 0), slope=0.5, color='k', transform=plt.gca().transAxes)

plt.ylim([0, 1])
plt.xlim([0, 1])
plt.show()
```
