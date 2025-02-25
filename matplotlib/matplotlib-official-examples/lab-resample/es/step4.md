# Actualizando los datos

Definiremos un método `update` que actualizará los datos. El método tomará el `ax` (eje) como parámetro de entrada. Actualizaremos la línea obteniendo el límite de vista y comprobando si el ancho del límite de vista es diferente de `delta`. Si el ancho del límite de vista es diferente de `delta`, actualizaremos `delta` y obtendremos `xstart` y `xend`. Luego estableceremos los datos en los datos con resolución reducida y dibujaremos el estado inactivo.

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```
