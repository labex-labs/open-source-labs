# Die Daten definieren und das Pfeildiagramm zeichnen

Der zweite Schritt besteht darin, die Daten zu definieren und das Pfeildiagramm mit der Funktion `make_arrow_graph()` zu zeichnen. Wir werden die Daten als Dictionary mit Wahrscheinlichkeiten für die Basen und Paarübergänge definieren. Wir werden auch die Größe des Diagramms auf 4 setzen und die Daten normalisieren.

```python
# Define the data
data = {
    'A': 0.4, 'T': 0.3, 'G': 0.6, 'C': 0.2,
    'AT': 0.4, 'AC': 0.3, 'AG': 0.2,
    'TA': 0.2, 'TC': 0.3, 'TG': 0.4,
    'CT': 0.2, 'CG': 0.3, 'CA': 0.2,
    'GA': 0.1, 'GT': 0.4, 'GC': 0.1,
}

# Plot the arrow graph
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size)

plt.show()
```
