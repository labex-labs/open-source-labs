# Erstellen eines einfachen Diagramms mit Standard-Einstellungen

Nachdem wir Matplotlib importiert haben, erstellen wir nun ein einfaches Diagramm mit Standard-Einstellungen, um zu verstehen, wie die Achsen und Tick-Labels (Markierungsbeschriftungen) standardmäßig positioniert werden.

## Grundlagen der Matplotlib-Komponenten

In Matplotlib besteht ein Diagramm aus mehreren Komponenten:

- **Figure (Figur)**: Der Gesamt-Container für das Diagramm
- **Axes (Achsenbereich)**: Der Bereich, in dem die Daten mit eigenem Koordinatensystem dargestellt werden
- **Axis (Achse)**: Die linienähnlichen Objekte, die das Koordinatensystem definieren
- **Ticks (Markierungen)**: Die Markierungen auf den Achsen, die bestimmte Werte markieren
- **Tick Labels (Markierungsbeschriftungen)**: Die Textbeschriftungen, die den Wert jeder Markierung angeben

Standardmäßig erscheinen die Tick-Labels der x-Achse am unteren Rand des Diagramms.

## Erstellen eines einfachen Diagramms

In einer neuen Zelle Ihres Notebooks erstellen wir ein einfaches Linien-Diagramm:

```python
# Create a figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.sin(x)

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='sin(x)')

# Add a title and labels
ax.set_title('A Simple Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (sin(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Notice that the x-axis tick labels are at the bottom of the plot by default.")
```

Wenn Sie diesen Code ausführen, sehen Sie ein Sinuswellen-Diagramm, bei dem die Tick-Labels der x-Achse am unteren Rand des Diagramms positioniert sind, was die Standard-Position in Matplotlib ist.

Nehmen Sie sich einen Moment Zeit, um zu beobachten, wie das Diagramm strukturiert ist und wo die Tick-Labels positioniert sind. Dieses Verständnis wird uns helfen, die Änderungen, die wir im nächsten Schritt vornehmen, besser zu verstehen.
