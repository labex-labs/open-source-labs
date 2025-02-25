# Utilisation des cartes de couleurs intégrées

Matplotlib fournit une variété de cartes de couleurs intégrées qui peuvent être utilisées pour représenter des données. Ces cartes de couleurs peuvent être accessibles en utilisant leurs noms, qui sont listés dans le module `matplotlib.cm`.

```python
import matplotlib.pyplot as plt

# Crée un graphique en utilisant la carte de couleurs 'viridis'
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
