# Erstellen eines Balkendiagramms mit einheitlichem Alpha-Wert

In diesem Schritt werden wir ein Balkendiagramm erstellen, bei dem alle Balken den gleichen Transparenzgrad haben, indem wir das Schlüsselwortargument `alpha` verwenden.

## Hinzufügen einer neuen Zelle

Fügen Sie eine neue Zelle zu Ihrem Jupyter Notebook hinzu, indem Sie auf die Schaltfläche "+" in der Symbolleiste klicken oder im Befehlsmodus "Esc" und dann "b" drücken.

## Erstellen des Balkendiagramms mit einheitlichem Alpha

Geben Sie den folgenden Code in die neue Zelle ein und führen Sie ihn aus:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Create the bar chart with alpha=0.5 for all bars
ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)

# Add a title and labels
ax.set_title("Bar Chart with Uniform Alpha Value (alpha=0.5)")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Verständnis des Codes und der Ausgabe

Nachdem Sie den Code ausgeführt haben, sollten Sie ein Balkendiagramm mit 20 Balken sehen. Jeder Balken ist entweder grün (positiv y-Wert) oder rot (negativ y-Wert) mit dem gleichen Transparenzgrad (alpha=0,5).

Lassen Sie uns die wichtigsten Teile analysieren:

1. `np.random.seed(19680801)` - Dies stellt sicher, dass die generierten Zufallszahlen jedes Mal gleich sind, wenn Sie den Code ausführen.

2. `x_values = list(range(20))` - Erstellt eine Liste von ganzen Zahlen von 0 bis 19 für die x-Achse.

3. `y_values = np.random.randn(20)` - Generiert 20 Zufallswerte aus einer Standardnormalverteilung für die y-Achse.

4. `facecolors = ['green' if y > 0 else 'red' for y in y_values]` - Diese Listenkomprehension weist positiven Werten Grün und negativen Werten Rot zu.

5. `ax.bar(..., alpha=0.5)` - Der wichtigste Teil, der einen einheitlichen Alpha-Wert von 0,5 für alle Balken festlegt.

Der einheitliche Alpha-Wert macht alle Balken gleichermaßen transparent, was nützlich sein kann, wenn Sie:

- Hintergrundgitterlinien durch die Balken hindurch sehen möchten
- Eine subtilere Visualisierung erstellen möchten
- Die visuelle Dominanz aller Elemente gleichermaßen reduzieren möchten

Im nächsten Schritt werden wir untersuchen, wie man unterschiedliche Alpha-Werte für verschiedene Balken festlegt.
