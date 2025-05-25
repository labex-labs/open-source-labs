# Criando um Mapa de Cores Simples

Para criar um mapa de cores simples, podemos usar a classe `ListedColormap` do módulo `matplotlib.colors`. Esta classe recebe uma lista de cores e cria um mapa de cores a partir delas.

```python
import matplotlib.colors as mcolors

# Define a list of colors
colors = ['red', 'green', 'blue']

# Create a ListedColormap object from the list of colors
cmap = mcolors.ListedColormap(colors)
```
