# Escribir clases personalizadas para dar estilo a las leyendas

En este paso, escribiremos clases personalizadas para dar estilo a las leyendas.

```python
# Definir los datos para el gráfico
class HandlerDashedLines(HandlerLineCollection):
    """
    Manejador personalizado para instancias de LineCollection.
    """
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # averiguar cuántas líneas hay
        numlines = len(orig_handle.get_segments())
        xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                             width, height, fontsize)
        leglines = []
        # dividir el espacio vertical donde irán las líneas
        # en partes iguales basadas en el número de líneas
        ydata = np.full_like(xdata, height / (numlines + 1))
        # para cada línea, crear la línea en la ubicación adecuada
        # y establecer el patrón de rayas
        for i in range(numlines):
            legline = Line2D(xdata, ydata * (numlines - i) - ydescent)
            self.update_prop(legline, orig_handle, legend)
            # establecer color, patrón de rayas y ancho de línea en el
            # de las líneas en linecollection
            try:
                color = orig_handle.get_colors()[i]
            except IndexError:
                color = orig_handle.get_colors()[0]
            try:
                dashes = orig_handle.get_dashes()[i]
            except IndexError:
                dashes = orig_handle.get_dashes()[0]
            try:
                lw = orig_handle.get_linewidths()[i]
            except IndexError:
                lw = orig_handle.get_linewidths()[0]
            if dashes[1] is not None:
                legline.set_dashes(dashes[1])
            legline.set_color(color)
            legline.set_transform(trans)
            legline.set_linewidth(lw)
            leglines.append(legline)
        return leglines

# Crear un gráfico con múltiples líneas
x = np.linspace(0, 5, 100)
fig, ax = plt.subplots()
colors = plt.rcParams['axes.prop_cycle'].by_key()['color'][:5]
styles = ['solid', 'dashed', 'dashed', 'dashed','solid']
for i, color, style in zip(range(5), colors, styles):
    ax.plot(x, np.sin(x) -.1 * i, c=color, ls=style)

# Crear artistas proxy y una leyenda
line = [[(0, 0)]]
lc = mcol.LineCollection(5 * line, linestyles=styles, colors=colors)
ax.legend([lc], ['multi-line'], handler_map={type(lc): HandlerDashedLines()},
          handlelength=2.5, handleheight=3)

# Mostrar el gráfico
plt.show()
```
