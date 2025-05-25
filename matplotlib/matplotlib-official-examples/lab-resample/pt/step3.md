# _Downsampling_ de dados

Definiremos um método `downsample` que fará o _downsample_ dos dados. O método receberá `xstart` e `xend` como parâmetros de entrada. Obteremos os pontos no intervalo de visualização e dilataremos a máscara em um para capturar os pontos logo fora do intervalo de visualização, a fim de não truncar a linha. Decidiremos quantos pontos descartar e mascarar os dados. Finalmente, faremos o _downsample_ dos dados e retornaremos `xdata` e `ydata`.

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
