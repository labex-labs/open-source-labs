# Crear subgráficos

A continuación, creamos los subgráficos utilizando `plt.subplot_mosaic`. Crearemos una cuadrícula de subgráficos de 3x2 y los etiquetaremos de la siguiente manera:

- El subgráfico de la esquina superior izquierda se etiquetará como "a)"
- El subgráfico de la esquina inferior izquierda se etiquetará como "b)"
- Los subgráficos de la esquina superior derecha e inferior derecha se etiquetarán como "c)" y "d)" respectivamente.

```python
fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']], layout='constrained')
```
