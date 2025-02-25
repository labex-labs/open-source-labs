# Crear un gráfico con una barra de color vertical

Comenzaremos creando un gráfico con una barra de color vertical. Generaremos algunos datos aleatorios utilizando `randn` de `numpy` y recortaremos los valores al rango de -1 a 1. Luego crearemos un objeto `AxesImage` utilizando `imshow` y la paleta de colores `coolwarm`. Finalmente, agregaremos un título al gráfico.

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
