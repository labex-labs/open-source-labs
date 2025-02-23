# Das Pfeildiagramm anpassen

Der dritte Schritt besteht darin, das Pfeildiagramm anzupassen. Wir können die Pfeileigenschaft zur Anzeige ändern, indem wir den Parameter `display` verwenden. Wir können auch die Form der Pfeile mit dem Parameter `shape` ändern. Wir können die Breite und den Abstand der Pfeile mit den Parametern `max_arrow_width` und `arrow_sep` entsprechend anpassen. Wir können die Transparenz der Pfeile mit dem Parameter `alpha` ändern. Wir können auch die Farbe des Labels mit dem Parameter `labelcolor` ändern.

```python
# Plot the arrow graph with customizations
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```
