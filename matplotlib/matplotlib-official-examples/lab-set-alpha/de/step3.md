# Erstellen eines Balkendiagramms mit unterschiedlichen Alpha-Werten

In diesem Schritt werden wir das Format `(matplotlib_color, alpha)` (Farbe in Matplotlib, Transparenzwert) verwenden, um jedem Balken basierend auf seinem Datenwert einen anderen Transparenzgrad zuzuweisen.

## Hinzufügen einer neuen Zelle

Fügen Sie eine neue Zelle zu Ihrem Jupyter Notebook hinzu, indem Sie auf die Schaltfläche "+" in der Symbolleiste klicken oder im Befehlsmodus "Esc" und dann "b" drücken.

## Erstellen des Balkendiagramms mit unterschiedlichen Alpha-Werten

Geben Sie den folgenden Code in die neue Zelle ein und führen Sie ihn aus:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data (using the same data as in Step 2 for comparison)
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Calculate alpha values based on the absolute y-values
# Normalize y values to get alpha values between 0.2 and 1.0
abs_y = [abs(y) for y in y_values]
max_abs_y = max(abs_y)
face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]

# Create color-alpha tuples for each bar
colors_with_alphas = list(zip(facecolors, face_alphas))

# Create the bar chart with varying alpha values
ax.bar(x_values, y_values, color=colors_with_alphas, edgecolor=edgecolors)

# Add a title and labels
ax.set_title("Bar Chart with Varying Alpha Values Based on Bar Height")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Verständnis des Codes und der Ausgabe

Nachdem Sie den Code ausgeführt haben, sollten Sie ein Balkendiagramm mit 20 Balken sehen. Jeder Balken hat einen Transparenzgrad, der proportional zu seinem absoluten y-Wert ist - höhere Balken sind undurchsichtiger, niedrigere Balken sind durchsichtiger.

Lassen Sie uns die wichtigsten Teile des Codes analysieren:

1. `abs_y = [abs(y) for y in y_values]` - Dies erstellt eine Liste der absoluten Werte aller y-Werte.

2. `max_abs_y = max(abs_y)` - Findet den maximalen absoluten Wert, um die Daten zu normalisieren.

3. `face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]` - Berechnet Alpha-Werte zwischen 0,2 und 1,0 basierend auf den normalisierten absoluten y-Werten.

4. `colors_with_alphas = list(zip(facecolors, face_alphas))` - Erstellt eine Liste von (Farbe, Alpha)-Tupeln, indem jede Farbe mit ihrem entsprechenden Alpha-Wert gepaart wird.

5. `ax.bar(..., color=colors_with_alphas, ...)` - Nutzt die (Farbe, Alpha)-Tupel, um jedem Balken einen anderen Alpha-Wert zuzuweisen.

Dieser Ansatz mit unterschiedlichen Transparenzgraden ist effektiv für:

- Das Betonen wichtigerer Datenpunkte
- Das Herunterspielen weniger wichtiger Datenpunkte
- Das Schaffen einer visuellen Hierarchie basierend auf den Datenwerten
- Das Hinzufügen einer zusätzlichen Informationsdimension zu Ihrer Visualisierung

Sie können deutlich sehen, wie die unterschiedlichen Alpha-Werte einen visuellen Effekt schaffen, bei dem die Größe eines Datenpunkts sowohl durch die Balkenhöhe als auch durch seine Undurchsichtigkeit betont wird.
