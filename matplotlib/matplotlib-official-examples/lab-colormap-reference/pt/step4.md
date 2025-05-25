# Invertendo Mapas de Cores

Matplotlib oferece a capacidade de inverter um mapa de cores adicionando `_r` ao nome do mapa de cores.

```python
import matplotlib.pyplot as plt

# Create a plot using the reversed 'viridis' color map
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```
