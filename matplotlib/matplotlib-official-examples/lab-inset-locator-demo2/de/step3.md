# Erstellen eines vergrößerten Einzugsbereichs mit einer Maßstäbe

Im ersten Teilplot werden wir einen vergrößerten Einzugsbereich mit einer Maßstäbe erstellen. Dies zeigt, wie man die `.zoomed_inset_axes`-Methode verwendet, um einen vergrößerten Einzugsbereich zu erstellen.

```python
# Set the aspect ratio of the plot to 1
ax.set_aspect(1)

# Create a zoomed inset in the upper right corner of the plot
axins = zoomed_inset_axes(ax, zoom=0.5, loc='upper right')

# Set the number of ticks on the inset axes
axins.yaxis.get_major_locator().set_params(nbins=7)
axins.xaxis.get_major_locator().set_params(nbins=7)

# Hide the tick labels on the inset axes
axins.tick_params(labelleft=False, labelbottom=False)

# Define a function to add a size bar to the plot
def add_sizebar(ax, size):
    asb = AnchoredSizeBar(ax.transData,
                          size,
                          str(size),
                          loc=8,
                          pad=0.1, borderpad=0.5, sep=5,
                          frameon=False)
    ax.add_artist(asb)

# Add a size bar to the main plot and the inset plot
add_sizebar(ax, 0.5)
add_sizebar(axins, 0.5)
```
