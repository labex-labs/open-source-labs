# Erstellen eines Streudiagramms mit Alpha-Werten

In diesem Schritt wenden wir unser Wissen über Alpha-Werte an, um ein Streudiagramm zu erstellen. Dies zeigt, wie Transparenz helfen kann, die Datendichte in Streudiagrammen mit überlappenden Punkten zu visualisieren.

## Hinzufügen einer neuen Zelle

Fügen Sie eine neue Zelle zu Ihrem Jupyter Notebook hinzu, indem Sie auf die Schaltfläche "+" in der Symbolleiste klicken oder im Befehlsmodus "Esc" und dann "b" drücken.

## Erstellen eines Streudiagramms mit Transparenz

Geben Sie den folgenden Code in die neue Zelle ein und führen Sie ihn aus:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create two clusters of points
cluster1_x = np.random.normal(0.3, 0.15, 500)
cluster1_y = np.random.normal(0.3, 0.15, 500)

cluster2_x = np.random.normal(0.7, 0.15, 500)
cluster2_y = np.random.normal(0.7, 0.15, 500)

# Combine the clusters
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])

# Create a scatter plot with alpha=0.5
scatter = ax.scatter(x, y, s=30, c='blue', alpha=0.5)

# Add a title and labels
ax.set_title("Scatter Plot with Alpha=0.5 Showing Data Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Verständnis des Codes und der Ausgabe

Nachdem Sie den Code ausgeführt haben, sollten Sie ein Streudiagramm mit zwei Punktclustern sehen. Jeder Punkt hat einen Transparenzgrad von 0,5, was es Ihnen ermöglicht, zu sehen, wo Punkte überlappen.

Lassen Sie uns die wichtigsten Teile des Codes analysieren:

1. `cluster1_x = np.random.normal(0.3, 0.15, 500)` - Generiert 500 zufällige x-Koordinaten, die einer Normalverteilung mit Mittelwert 0,3 und Standardabweichung 0,15 folgen.

2. `cluster1_y = np.random.normal(0.3, 0.15, 500)` - Generiert 500 zufällige y-Koordinaten für das erste Cluster.

3. `cluster2_x` und `cluster2_y` - Generieren in ähnlicher Weise Koordinaten für das zweite Cluster, das um (0,7, 0,7) zentriert ist.

4. `ax.scatter(..., alpha=0.5)` - Erstellt ein Streudiagramm mit Punkten in 50 % Opazität.

Die Vorteile der Verwendung von Alpha in Streudiagrammen sind:

1. **Dichtevisualisierung**: Bereiche, in denen viele Punkte überlappen, erscheinen dunkler und zeigen so die Datendichte.

2. **Verringerung von Überplottung**: Ohne Transparenz würden überlappende Punkte einander vollständig verdecken.

3. **Mustererkennung**: Transparenz hilft bei der Identifizierung von Clustern und Mustern in den Daten.

Beachten Sie, wie Bereiche mit mehr überlappenden Punkten in der Visualisierung dunkler erscheinen. Dies ist eine leistungsstarke Methode, um Datendichte zu visualisieren, ohne zusätzliche Techniken wie Dichteschätzung zu benötigen.
