# Crear los fotogramas de la animación

Ahora crearemos los fotogramas de la animación. Utilizaremos un bucle `for` para generar 60 fotogramas. En cada iteración del bucle, actualizaremos los datos de `x` e `y` y luego crearemos un nuevo objeto de imagen utilizando el método `imshow`. Luego agregaremos el objeto de imagen a la lista `ims`.

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # show an initial one first
    ims.append([im])
```
