# Criando Mapas de Cores Personalizados

Matplotlib também oferece a capacidade de criar mapas de cores personalizados. Isso pode ser útil quando os mapas de cores embutidos não fornecem a representação desejada dos dados.

```python
import matplotlib.colors as mcolors

# Define a list of colors and their corresponding values
colors = [(0, 'red'), (0.5, 'green'), (1, 'blue')]

# Create a LinearSegmentedColormap object from the list of colors
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', colors)
```
