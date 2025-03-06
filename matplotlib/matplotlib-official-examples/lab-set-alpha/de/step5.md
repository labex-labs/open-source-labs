# Erstellen einer kombinierten Visualisierung mit verschiedenen Alpha-Techniken

In diesem letzten Schritt werden wir mehrere Techniken kombinieren, um eine komplexere Visualisierung zu erstellen, die sowohl einheitliche als auch variierende Alpha-Werte in einem Diagramm zeigt.

## Hinzufügen einer neuen Zelle

Fügen Sie eine neue Zelle zu Ihrem Jupyter Notebook hinzu, indem Sie auf die Schaltfläche "+" in der Symbolleiste klicken oder im Befehlsmodus "Esc" und dann "b" drücken.

## Erstellen einer kombinierten Visualisierung

Geben Sie den folgenden Code in die neue Zelle ein und führen Sie ihn aus:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## Verständnis des Codes und der Ausgabe

Nachdem Sie den Code ausgeführt haben, sollten Sie ein Diagramm mit zwei nebeneinander liegenden Teilplots sehen:

1. **Linker Teilplot (Einheitlicher Alpha-Wert)**: Zeigt drei trigonometrische Funktionen, die mit demselben Alpha-Wert (0,7) geplottet wurden.

2. **Rechter Teilplot (Variierender Alpha-Wert)**: Zeigt ein Streudiagramm, bei dem:
   - Die x-Koordinate der Eingabewert ist.
   - Die y-Koordinate sin(x)cos(x) ist.
   - Die Größe jedes Punkts basierend auf dem absoluten y-Wert variiert.
   - Die Farbe jedes Punkts basierend auf dem y-Wert variiert.
   - Der Alpha-Wert (Transparenz) jedes Punkts basierend auf dem absoluten y-Wert variiert.

Lassen Sie uns die wichtigsten Teile des Codes analysieren:

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` - Erstellt ein Diagramm mit zwei nebeneinander liegenden Teilplots.

2. Für den ersten Teilplot:

   - `ax1.plot(..., alpha=0.7)` - Verwendet einen einheitlichen Alpha-Wert für alle drei Linien.

3. Für den zweiten Teilplot:
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` - Berechnet variierende Alpha-Werte zwischen 0,3 und 1,0.
   - `ax2.scatter(..., alpha=alphas)` - Verwendet variierende Alpha-Werte für die Streupunkte.

Diese Kombination von Techniken zeigt, wie Alpha-Werte auf verschiedene Weise eingesetzt werden können, um Visualisierungen zu verbessern:

- **Einheitlicher Alpha-Wert** ist hilfreich, wenn Sie mehrere überlappende Elemente gleicher Wichtigkeit darstellen müssen.

- **Variierender Alpha-Wert** ist nützlich, wenn Sie bestimmte Datenpunkte basierend auf ihren Werten hervorheben möchten.

Durch das Beherrschen dieser Techniken können Sie effektivere und visuell ansprechende Datenvisualisierungen erstellen.
