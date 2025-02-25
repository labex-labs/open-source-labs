# Actualizar los colores del histograma

El método `histogram` devuelve (entre otras cosas) un objeto `patches`. Esto nos da acceso a las propiedades de los objetos dibujados. Con esto, podemos editar el histograma según nuestras preferencias. Cambiemos el color de cada barra según su valor `y`.

```python
# N es la cuenta en cada intervalo, bins es el límite inferior del intervalo
N, bins, patches = axs[0].hist(dist1, bins=n_bins)

# Codificaremos el color por altura, pero podrías usar cualquier escalar
fracs = N / N.max()

# necesitamos normalizar los datos a 0..1 para el rango completo de la mapa de colores
norm = colors.Normalize(fracs.min(), fracs.max())

# Ahora, recorreremos nuestros objetos y estableceremos el color de cada uno en consecuencia
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# También podemos normalizar nuestras entradas por el número total de conteos
axs[1].hist(dist1, bins=n_bins, density=True)

# Ahora formateamos el eje y para mostrar el porcentaje
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()
```
