# Configurar el gráfico

Primero, debemos configurar el gráfico con dos subgráficos. Utilizaremos la función `subplots` para crear una cuadrícula de subgráficos de 2x2, y luego definiremos las coordenadas x e y de dos puntos.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
