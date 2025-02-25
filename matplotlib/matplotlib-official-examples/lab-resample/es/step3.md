# Reduciendo la resolución de los datos

Definiremos un método `downsample` que reducirá la resolución de los datos. El método tomará `xstart` y `xend` como parámetros de entrada. Obtendremos los puntos en el rango de vista y dilataremos la máscara en uno para capturar los puntos justo fuera del rango de vista y no truncar la línea. Determinaremos cuántos puntos eliminar y aplicaremos la máscara a los datos. Finalmente, reduciremos la resolución de los datos y devolveremos `xdata` e `ydata`.

```python
def downsample(self, xstart, xend):
    # get the points in the view range
    mask = (self.origXData > xstart) & (self.origXData < xend)
    # dilate the mask by one to catch the points just outside
    # of the view range to not truncate the line
    mask = np.convolve([1, 1, 1], mask, mode='same').astype(bool)
    # sort out how many points to drop
    ratio = max(np.sum(mask) // self.max_points, 1)

    # mask data
    xdata = self.origXData[mask]
    ydata = self.origYData[mask]

    # downsample data
    xdata = xdata[::ratio]
    ydata = ydata[::ratio]

    print(f"using {len(ydata)} of {np.sum(mask)} visible points")

    return xdata, ydata
```
