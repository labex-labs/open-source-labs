# Écrire des classes personnalisées pour styliser les légendes

Dans cette étape, nous allons écrire des classes personnalisées pour styliser les légendes.

```python
# Define data for the chart
class HandlerDashedLines(HandlerLineCollection):
    """
    Gestionnaire personnalisé pour les instances de LineCollection.
    """
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # déterminer combien de lignes il y a
        numlines = len(orig_handle.get_segments())
        xdata, xdata_marker = self.get_xdata(legend, xdescent, ydescent,
                                             width, height, fontsize)
        leglines = []
        # diviser l'espace vertical où les lignes seront placées
        # en parties égales en fonction du nombre de lignes
        ydata = np.full_like(xdata, height / (numlines + 1))
        # pour chaque ligne, créer la ligne à l'emplacement approprié
        # et définir le motif de tirets
        for i in range(numlines):
            legline = Line2D(xdata, ydata * (numlines - i) - ydescent)
            self.update_prop(legline, orig_handle, legend)
            # définir la couleur, le motif de tirets et la largeur de ligne
            # sur celle des lignes dans linecollection
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

# Create a chart with multiple lines
x = np.linspace(0, 5, 100)
fig, ax = plt.subplots()
colors = plt.rcParams['axes.prop_cycle'].by_key()['color'][:5]
styles = ['solide', 'tireté', 'tireté', 'tireté','solide']
for i, color, style in zip(range(5), colors, styles):
    ax.plot(x, np.sin(x) -.1 * i, c=color, ls=style)

# Create proxy artists and a legend
line = [[(0, 0)]]
lc = mcol.LineCollection(5 * line, linestyles=styles, colors=colors)
ax.legend([lc], ['multi-ligne'], handler_map={type(lc): HandlerDashedLines()},
          handlelength=2.5, handleheight=3)

# Display the chart
plt.show()
```
