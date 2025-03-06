# Erstellung und Konfiguration des Diagramms mit unterbrochener Achse

In diesem Schritt werden wir die eigentliche Struktur des Diagramms mit unterbrochener Achse erstellen. Ein Diagramm mit unterbrochener Achse besteht aus mehreren Teilplots, die verschiedene Bereiche derselben Daten anzeigen. Wir werden diese Teilplots so konfigurieren, dass unsere Hauptdaten und Ausreißer effektiv dargestellt werden.

## Erstellung der Teilplots

Zunächst müssen wir zwei vertikal angeordnete Teilplots erstellen. Der obere Teilplot wird unsere Ausreißer anzeigen, während der untere Teilplot die Mehrheit unserer Datenpunkte zeigen wird.

Erstellen Sie eine neue Zelle in Ihrem Notebook und fügen Sie den folgenden Code hinzu:

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Add a main title to the figure
fig.suptitle('Broken Axis Plot Example', fontsize=16)

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Display the figure to see both subplots
plt.tight_layout()
plt.show()
```

![broken-axis-plot](../assets/screenshot-20250306-cawcMZv3@2x.png)

Wenn Sie diese Zelle ausführen, sollten Sie ein Diagramm mit zwei Teilplots sehen, die beide dieselben Daten anzeigen. Beachten Sie, wie die Ausreißer den Rest der Daten in beiden Plots komprimieren, was es schwierig macht, die Details der Mehrheit der Datenpunkte zu sehen. Dies ist genau das Problem, das wir mit einem Diagramm mit unterbrochener Achse lösen möchten.

## Konfiguration der y-Achsengrenzen

Jetzt müssen wir jeden Teilplot so konfigurieren, dass er sich auf einen bestimmten Bereich von y-Werten konzentriert. Der obere Teilplot wird sich auf den Bereich der Ausreißer konzentrieren, während der untere Teilplot sich auf den Bereich der Hauptdaten konzentrieren wird.

Erstellen Sie eine neue Zelle und fügen Sie den folgenden Code hinzu:

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Add a title to each subplot
ax1.set_title('Outlier Region')
ax2.set_title('Main Data Region')

# Display the figure with adjusted y-axis limits
plt.tight_layout()
plt.show()
```

Wenn Sie diese Zelle ausführen, sollten Sie sehen, dass sich jeder Teilplot jetzt auf einen anderen Bereich von y-Werten konzentriert. Der obere Plot zeigt nur die Ausreißer, und der untere Plot zeigt nur die Hauptdaten. Dies verbessert bereits die Visualisierung, aber um es zu einem richtigen Diagramm mit unterbrochener Achse zu machen, müssen wir noch einige Konfigurationen hinzufügen.

## Ausblenden der Achsenlinien und Anpassen der Tick-Markierungen

Um die Illusion einer "unterbrochenen" Achse zu schaffen, müssen wir die verbindenden Achsenlinien zwischen den beiden Teilplots ausblenden und die Positionen der Tick-Markierungen anpassen.

Erstellen Sie eine neue Zelle und fügen Sie den folgenden Code hinzu:

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add labels to the plot
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')

plt.tight_layout()
plt.show()
```

Wenn Sie diese Zelle ausführen, sollten Sie sehen, dass das Diagramm jetzt die Achsenlinien zwischen den beiden Teilplots ausblendet, was ein saubereres Erscheinungsbild schafft. Die Tick-Markierungen der x-Achse sind jetzt korrekt positioniert, wobei die Beschriftungen nur am unteren Rand angezeigt werden.

An diesem Punkt haben wir erfolgreich ein einfaches Diagramm mit unterbrochener Achse erstellt. Im nächsten Schritt werden wir noch einige Feinheiten hinzufügen, um den Betrachtern klar zu machen, dass die Achse unterbrochen ist.
