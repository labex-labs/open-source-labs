# Speichern und Teilen Ihres Diagramms

Der letzte Schritt besteht darin, Ihr angepasstes Diagramm zu speichern, damit Sie es in Berichten, Präsentationen einbinden oder es mit anderen teilen können.

## Speichern von Diagrammen in verschiedenen Formaten

Matplotlib ermöglicht es Ihnen, Diagramme in verschiedenen Formaten zu speichern, darunter PNG, JPG, PDF, SVG und viele mehr. Lassen Sie uns lernen, wie wir unser Diagramm in verschiedenen Formaten speichern können:

```python
# Create a plot similar to our previous customized one
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels
ax.set_title('Plot with X-Axis Labels at the Top', fontsize=14)
ax.set_xlabel('X-axis at the top')
ax.set_ylabel('Y-axis')

# Add grid and legend
ax.grid(True)
ax.legend()

# Save the figure in different formats
plt.savefig('plot_with_top_xlabels.png', dpi=300, bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.pdf', bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.svg', bbox_inches='tight')

# Show the plot
plt.show()

print("The plot has been saved in PNG, PDF, and SVG formats in the current directory.")
```

Wenn Sie diesen Code ausführen, wird das Diagramm in drei verschiedenen Formaten gespeichert:

- PNG: Ein Rasterbildformat, das gut für das Web und die allgemeine Verwendung geeignet ist
- PDF: Ein Vektorgrafikformat, das ideal für Publikationen und Berichte ist
- SVG: Ein Vektorgrafikformat, das hervorragend für das Web und bearbeitbare Grafiken geeignet ist

Die Dateien werden im aktuellen Arbeitsverzeichnis Ihres Jupyter-Notebooks gespeichert.

## Verständnis der Speicherparameter

Lassen Sie uns die Parameter untersuchen, die mit `savefig()` verwendet werden:

- `dpi=300`: Legt die Auflösung (Punkte pro Zoll) für Rasterformate wie PNG fest
- `bbox_inches='tight'`: Passt automatisch die Diagrammgrenzen an, um alle Elemente ohne unnötigen Leerraum einzuschließen

## Anzeigen der gespeicherten Dateien

Sie können die gespeicherten Dateien anzeigen, indem Sie im Jupyter-Dateibrowser navigieren:

1. Klicken Sie auf das "Jupyter"-Logo oben links.
2. Im Dateibrowser sollten Sie die gespeicherten Bilddateien sehen.
3. Klicken Sie auf eine beliebige Datei, um sie anzuzeigen oder herunterzuladen.

## Zusätzliche Optionen zum Exportieren von Diagrammen

Für eine bessere Kontrolle über das gespeicherte Diagramm können Sie die Diagrammgröße anpassen, den Hintergrund einstellen oder die DPI (Auflösung) nach Ihren Bedürfnissen ändern:

```python
# Control the background color and transparency
fig.patch.set_facecolor('white')  # Set figure background color
fig.patch.set_alpha(0.8)          # Set background transparency

# Save with custom settings
plt.savefig('custom_background_plot.png',
            dpi=400,              # Higher resolution
            facecolor=fig.get_facecolor(),  # Use the figure's background color
            edgecolor='none',     # No edge color
            bbox_inches='tight',  # Tight layout
            pad_inches=0.1)       # Add a small padding

print("A customized plot has been saved with specialized export settings.")
```

Dies zeigt, wie Sie Diagramme mit präziser Kontrolle über das Ausgabeformat und das Erscheinungsbild speichern können.
