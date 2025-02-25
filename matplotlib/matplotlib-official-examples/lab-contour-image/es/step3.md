# Crear la imagen de contorno

En este paso, creará la imagen de contorno utilizando las funciones contour y contourf de Matplotlib.

```python
# Aumente el límite superior para evitar errores de truncamiento.
levels = np.arange(-2.0, 1.601, 0.4)

norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
cmap = cm.PRGn

fig, _axs = plt.subplots(nrows=2, ncols=2)
fig.subplots_adjust(hspace=0.3)
axs = _axs.flatten()

cset1 = axs[0].contourf(X, Y, Z, levels, norm=norm,
                        cmap=cmap.resampled(len(levels) - 1))
# No es necesario, pero para el mapa de colores, solo necesitamos
# el número de niveles menos 1. Para evitar errores de discretización, use
# este número o un número grande como el predeterminado (256).

# Si queremos líneas así como regiones rellenas, debemos llamar
# a contour por separado; no intente cambiar el color de borde o el ancho de borde
# de los polígonos en las colecciones devueltas por contourf.
# Utilice los niveles de salida de la llamada anterior para garantizar que son los mismos.

cset2 = axs[0].contour(X, Y, Z, cset1.levels, colors='k')

# Realmente no necesitamos líneas de contorno discontinuas para indicar
# regiones negativas, así que las desactivaremos.

for c in cset2.collections:
    c.set_linestyle('solid')

# Aquí es más fácil hacer una llamada separada a contour que
# configurar una matriz de colores y anchos de línea.
# Estamos creando una línea verde gruesa como un contorno de cero.
# Especifique el nivel cero como una tupla con solo 0 en ella.

cset3 = axs[0].contour(X, Y, Z, (0,), colors='g', linewidths=2)
axs[0].set_title('Contornos rellenos')
fig.colorbar(cset1, ax=axs[0])


axs[1].imshow(Z, extent=extent, cmap=cmap, norm=norm)
axs[1].contour(Z, levels, colors='k', origin='upper', extent=extent)
axs[1].set_title("Imagen, origen 'upper'")

axs[2].imshow(Z, origin='lower', extent=extent, cmap=cmap, norm=norm)
axs[2].contour(Z, levels, colors='k', origin='lower', extent=extent)
axs[2].set_title("Imagen, origen 'lower'")

# Usaremos la interpolación "nearest" aquí para mostrar los actuales
# píxeles de la imagen.
# Tenga en cuenta que las líneas de contorno no se extienden hasta el borde del cuadro.
# Esto es intencional. Los valores de Z se definen en el centro de cada
# píxel de imagen (cada bloque de color en el siguiente subtrayecto), por lo que
# el dominio que se contorna no se extiende más allá de estos centros de píxeles.
im = axs[3].imshow(Z, interpolation='nearest', extent=extent,
                   cmap=cmap, norm=norm)
axs[3].contour(Z, levels, colors='k', origin='image', extent=extent)
ylim = axs[3].get_ylim()
axs[3].set_ylim(ylim[::-1])
axs[3].set_title("Origen de rc, eje y invertido")
fig.colorbar(im, ax=axs[3])

fig.tight_layout()
plt.show()
```
