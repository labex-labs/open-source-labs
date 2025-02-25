# Usando mapas de colores integrados

Matplotlib proporciona una variedad de mapas de colores integrados que se pueden utilizar para representar datos. Estos mapas de colores se pueden acceder utilizando sus nombres, que se enumeran en el módulo `matplotlib.cm`.

```python
import matplotlib.pyplot as plt

# Crea un gráfico utilizando el mapa de colores 'viridis'
plt.imshow(data, cmap='viridis')
plt.colorbar()
```
