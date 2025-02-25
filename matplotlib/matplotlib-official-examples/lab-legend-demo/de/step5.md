# Benutzereigene Klassen schreiben, um Legenden zu stylisieren

In diesem Schritt werden wir benutzereigene Klassen schreiben, um Legenden zu stylisieren.

```python
# Definiere Daten für das Diagramm
class HandlerDashedLines(HandlerLineCollection):
    """
    Benutzerspezifischer Handler für LineCollection-Instanzen.
    """
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # ermittle, wie viele Linien es gibt
        numlines = len(orig_handle.get_segments())
        xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                             width, height, fontsize)
        leglines = []
        # teile den vertikalen Raum, in dem die Linien platziert werden,
        # in gleich große Teile basierend auf der Anzahl der Linien auf
        ydata = np.full_like(xdata, height / (numlines + 1))
        # für jede Linie erzeuge die Linie an der richtigen Position
        # und setze das Strichelduster
        for i in range(numlines):
            legline = Line2D(xdata, ydata * (numlines - i) - ydescent)
            self.update_prop(legline, orig_handle, legend)
            # setze Farbe, Strichelduster und Linienstärke auf die
            # der Linien in der LineCollection
            versuche:
                color = orig_handle.get_colors()[i]
            außer:
                color = orig_handle.get_colors()[0]
            versuche:
                dashes = orig_handle.get_dashes()[i]
            außer:
                dashes = orig_handle.get_dashes()[0]
            versuche:
                lw = orig_handle.get_linewidths()[i]
            außer:
                lw = orig_handle.get_linewidths()[0]
            wenn das zweite Element von dashes nicht None ist:
                legline.set_dashes(dashes[1])
            legline.set_color(color)
            legline.set_transform(trans)
            legline.set_linewidth(lw)
            leglines.append(legline)
        return leglines

# Erstelle ein Diagramm mit mehreren Linien
x = np.linspace(0, 5, 100)
fig, ax = plt.subplots()
colors = plt.rcParams['axes.prop_cycle'].by_key()['color'][:5]
styles = ['solid', 'dashed', 'dashed', 'dashed','solid']
for i, color, style in zip(range(5), colors, styles):
    ax.plot(x, np.sin(x) -.1 * i, c=color, ls=style)

# Erstelle Proxy-Künstler und eine Legende
line = [[(0, 0)]]
lc = mcol.LineCollection(5 * line, linestyles=styles, colors=colors)
ax.legend([lc], ['multi-line'], handler_map={type(lc): HandlerDashedLines()},
          handlelength=2.5, handleheight=3)

# Zeige das Diagramm an
plt.show()
```
