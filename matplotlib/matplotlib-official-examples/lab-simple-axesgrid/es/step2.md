# Crear un objeto de figura y un objeto ImageGrid

A continuación, creamos un objeto `figure` usando la función `plt.figure` y pasamos el argumento `figsize` para establecer el tamaño de la figura. Luego creamos un objeto `ImageGrid` usando la función `ImageGrid` y pasamos el `figure`, `111` como argumento de subtrama, `(2, 2)` como argumento `nrows_ncols` para crear una cuadrícula de 2x2 de ejes y `0.1` como argumento `axes_pad` para establecer el relleno entre los ejes.

```python
fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(2, 2), axes_pad=0.1)
```
