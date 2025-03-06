# Verschieben der Tick-Labels der x-Achse nach oben

Nachdem wir die Standard-Positionierung der Tick-Labels verstanden haben, verschieben wir nun die Tick-Labels der x-Achse nach oben im Diagramm.

## Grundlagen der Tick-Parameter

Matplotlib bietet die Methode `tick_params()`, um das Erscheinungsbild von Tick-Markierungen und Tick-Labels zu steuern. Mit dieser Methode können wir:

- Tick-Markierungen und Tick-Labels anzeigen/ausblenden
- Ihre Position ändern (oben, unten, links, rechts)
- Ihre Größe, Farbe und andere Eigenschaften anpassen

## Erstellen eines Diagramms mit Tick-Labels der x-Achse oben

Erstellen wir ein neues Diagramm, bei dem die Tick-Labels der x-Achse nach oben verschoben sind:

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.cos(x)

# Plot the data
ax.plot(x, y, marker='s', linestyle='-', color='green', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',         # Apply changes to the x-axis
    top=True,         # Show ticks on the top side
    labeltop=True,    # Show tick labels on the top side
    bottom=False,     # Hide ticks on the bottom side
    labelbottom=False # Hide tick labels on the bottom side
)

# Add a title and labels
ax.set_title('Cosine Wave with X-Axis Tick Labels at the Top')
ax.set_xlabel('X-axis (now at the top!)')
ax.set_ylabel('Y-axis (cos(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Now the x-axis tick labels are at the top of the plot!")
```

Wenn Sie diesen Code ausführen, sehen Sie ein Kosinuswellen-Diagramm, bei dem die Tick-Labels der x-Achse oben im Diagramm positioniert sind.

Beachten Sie, wie die Methode `tick_params()` mit mehreren Parametern verwendet wird:

- `axis='x'`: Gibt an, dass wir die x-Achse ändern möchten
- `top=True` und `labeltop=True`: Macht Tick-Markierungen und -Labels oben sichtbar
- `bottom=False` und `labelbottom=False`: Blendet Tick-Markierungen und -Labels unten aus

Dadurch erhalten wir eine klare Ansicht der Daten, bei der die x-Achsen-Labels oben statt unten positioniert sind.
