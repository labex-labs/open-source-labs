# Weitere Anpassung des Diagramms

Nachdem wir die Tick-Labels der x-Achse nach oben verschoben haben, passen wir unser Diagramm nun weiter an, um es visuell ansprechender und informativer zu gestalten.

## Fortgeschrittene Techniken zur Diagrammanpassung

Matplotlib bietet zahlreiche Optionen zur Anpassung von Diagrammen. Betrachten wir einige dieser Optionen:

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate some data with more points for a smoother curve
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot multiple datasets
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Fill the area between curves
ax.fill_between(x, y1, y2, where=(y1 > y2), alpha=0.3, color='green', interpolate=True)
ax.fill_between(x, y1, y2, where=(y1 <= y2), alpha=0.3, color='purple', interpolate=True)

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

# Add title and labels with custom styles
ax.set_title('Sine and Cosine Functions with Customized X-Axis Labels at the Top',
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Angle (radians)', fontsize=12)
ax.set_ylabel('Function Value', fontsize=12)

# Add a grid and customize its appearance
ax.grid(True, linestyle='--', alpha=0.7, which='both')

# Customize the axis limits
ax.set_ylim(-1.2, 1.2)

# Add a legend with custom location and style
ax.legend(loc='upper right', fontsize=12, framealpha=0.8)

# Add annotations to highlight important points
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=10, ha='center')

# Display the plot
plt.tight_layout()  # Adjust spacing for better appearance
plt.show()

print("We have created a fully customized plot with x-axis tick labels at the top!")
```

Wenn Sie diesen Code ausführen, sehen Sie ein viel aufwändigeres und professioneller aussehendes Diagramm mit:

- Zwei Kurven (Sinus und Kosinus)
- Farbigen Bereichen zwischen den Kurven
- Angepassten Tick-Labels (mit π-Notation)
- Anmerkungen, die wichtige Merkmale markieren
- Besseren Abständen und Stilen

Beachten Sie, wie wir die Tick-Labels der x-Achse mit der Methode `tick_params()` oben belassen haben, aber das Diagramm mit zusätzlichen Anpassungen verbessert haben.

## Verständnis der Anpassungen

Lassen Sie uns einige der wichtigen Anpassungen, die wir vorgenommen haben, analysieren:

1. `fill_between()`: Erstellt farbige Bereiche zwischen den Sinus- und Kosinus-Kurven
2. `set_xticks()` und `set_xticklabels()`: Passt die Positionen und Beschriftungen der Tick-Markierungen an
3. `tight_layout()`: Passt die Abstände im Diagramm automatisch für ein besseres Erscheinungsbild an
4. `annotate()`: Fügt Text mit einem Pfeil hinzu, der auf einen bestimmten Punkt zeigt
5. Angepasste Schriftarten, Farben und Stile für verschiedene Elemente

Diese Anpassungen zeigen, wie Sie visuell ansprechende und informativer Diagramme erstellen können, während Sie die Tick-Labels der x-Achse oben belassen.
