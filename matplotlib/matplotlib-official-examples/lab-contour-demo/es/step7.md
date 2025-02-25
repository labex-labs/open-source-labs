# Utilizar una mapa de colores para especificar los colores de los contornos

Podemos utilizar un mapa de colores para especificar los colores de las líneas de contorno.

```python
fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', origin='lower',
               cmap=cm.gray, extent=(-3, 3, -2, 2))
levels = np.arange(-1.2, 1.6, 0.2)
CS = ax.contour(Z, levels, origin='lower', cmap='flag', extend='both',
                linewidths=2, extent=(-3, 3, -2, 2))

# Aumentar el grosor del contorno cero.
CS.collections[6].set_linewidth(4)

ax.clabel(CS, levels[1::2],  # etiquetar cada segundo nivel
          inline=True, fmt='%1.1f', fontsize=14)

# crear una barra de colores para las líneas de contorno
CB = fig.colorbar(CS, shrink=0.8)

ax.set_title('Lines with colorbar')

# Todavía podemos agregar una barra de colores para la imagen también.
CBI = fig.colorbar(im, orientation='horizontal', shrink=0.8)

# Esto hace que la barra de colores original se vea un poco fuera de lugar,
# así que mejoraremos su posición.

l, b, w, h = ax.get_position().bounds
ll, bb, ww, hh = CB.ax.get_position().bounds
CB.ax.set_position([ll, b + 0.1*h, ww, h*0.8])
```
