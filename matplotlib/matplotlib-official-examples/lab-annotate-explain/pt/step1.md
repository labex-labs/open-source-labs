# Configurar o gráfico

Primeiramente, precisamos configurar o gráfico com dois subplots. Usaremos a função `subplots` para criar uma grade 2x2 de subplots e, em seguida, definiremos as coordenadas x e y de dois pontos.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, axs = plt.subplots(2, 2)
x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7
```
