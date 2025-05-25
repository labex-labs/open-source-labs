# Usando Mapas de Cores Embutidos

Matplotlib fornece uma variedade de mapas de cores embutidos que podem ser usados para representar dados. Esses mapas de cores podem ser acessados usando seus nomes, que estão listados no módulo `matplotlib.cm`.

```python
import matplotlib.pyplot as plt

# Create a plot using the 'viridis' color map
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
