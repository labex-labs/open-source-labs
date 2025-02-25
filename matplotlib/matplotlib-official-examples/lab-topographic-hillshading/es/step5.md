# Crear la gráfica

Creamos una cuadrícula de gráficas de 4x3 para mostrar las gráficas con sombreado de colinas con diferentes modos de mezcla y exageración vertical. Primero mostramos la imagen de intensidad de sombreado de colinas en la primera fila, y luego colocamos gráficas con sombreado de colinas con diferentes modos de mezcla en el resto de las filas. Utilizamos un bucle `for` para iterar a través de los diferentes valores de exageración vertical y modos de mezcla.

```python
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(8, 9))
plt.setp(axs.flat, xticks=[], yticks=[])

for col, ve in zip(axs.T, [0.1, 1, 10]):
    col[0].imshow(ls.hillshade(z, vert_exag=ve, dx=dx, dy=dy), cmap='gray')
    for ax, mode in zip(col[1:], ['hsv', 'overlay','soft']):
        rgb = ls.shade(z, cmap=cmap, blend_mode=mode,
                       vert_exag=ve, dx=dx, dy=dy)
        ax.imshow(rgb)
```
