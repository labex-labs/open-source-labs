# Usando hojas de estilo

Otra forma de cambiar la apariencia visual de las gráficas es establecer los rcParams en una hoja de estilo e importar esa hoja de estilo con `matplotlib.style.use`. Una hoja de estilo es un archivo que contiene un conjunto de rcParams relacionados con el estilo de una gráfica. Matplotlib proporciona una serie de estilos predefinidos que puedes utilizar. Por ejemplo, el estilo "ggplot" emula la estética de la biblioteca ggplot en R. Puedes aplicar una hoja de estilo de la siguiente manera:

```python
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')
```

También puedes definir tus propios estilos personalizados y utilizarlos llamando a `.style.use` con la ruta o la URL de la hoja de estilo.
