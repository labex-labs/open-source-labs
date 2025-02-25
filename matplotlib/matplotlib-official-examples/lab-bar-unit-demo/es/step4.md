# Definir los parámetros del gráfico de barras

El siguiente paso es definir los parámetros para el gráfico de barras. Definiremos las ubicaciones x para los grupos, el ancho de las barras y las etiquetas para las marcas de los ejes x.

```python
ind = np.arange(N)    # las ubicaciones x para los grupos
width = 0.35         # el ancho de las barras
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```
