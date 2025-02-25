# Invirtiendo mapas de colores

Matplotlib permite invertir un mapa de colores agregando `_r` al nombre del mapa de colores.

```python
import matplotlib.pyplot as plt

# Crea un gráfico utilizando el mapa de colores 'viridis' invertido
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```
