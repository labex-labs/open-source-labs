# Inversion des cartes de couleurs

Matplotlib permet d'inverser une carte de couleurs en ajoutant `_r` au nom de la carte de couleurs.

```python
import matplotlib.pyplot as plt

# Crée un graphique en utilisant la carte de couleurs inversée 'viridis'
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```
