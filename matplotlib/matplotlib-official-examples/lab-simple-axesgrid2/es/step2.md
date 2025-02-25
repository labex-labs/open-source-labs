# Crear una Figura y un ImageGrid

A continuación, creamos una figura y un ImageGrid con el parámetro `nrows_ncols` para definir el número de filas y columnas de la cuadrícula.

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # similar a subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```
