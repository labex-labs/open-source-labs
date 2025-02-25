# Crear un gráfico con una barra de color horizontal

Ahora crearemos un gráfico con una barra de color horizontal. Seguiremos los mismos pasos que en el Paso 2, pero esta vez usaremos la paleta de colores `afmhot` y estableceremos la orientación de la barra de color en horizontal.

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
