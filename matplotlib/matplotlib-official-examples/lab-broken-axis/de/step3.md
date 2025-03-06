# Hinzufügen von Feinheiten zum Diagramm mit unterbrochener Achse

In diesem letzten Schritt werden wir unserem Diagramm mit unterbrochener Achse Feinheiten hinzufügen, um deutlich zu machen, dass die y-Achse unterbrochen ist. Wir werden diagonale Linien zwischen den Teilplots hinzufügen, um die Unterbrechung anzuzeigen, und das Gesamtaussehen des Diagramms mit geeigneten Beschriftungen und einem Gitter verbessern.

## Hinzufügen von diagonalen Unterbrechungslinien

Um visuell anzuzeigen, dass die Achse unterbrochen ist, werden wir diagonale Linien zwischen den beiden Teilplots hinzufügen. Dies ist eine gängige Konvention, die den Betrachtern hilft zu verstehen, dass ein Teil der Achse weggelassen wurde.

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

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

Wenn Sie diese Zelle ausführen, sollten Sie das vollständige Diagramm mit unterbrochener Achse sehen, mit diagonalen Linien, die die Unterbrechung der y-Achse anzeigen. Das Diagramm hat jetzt einen Titel, Achsenbeschriftungen und Gitterlinien, um die Lesbarkeit zu verbessern.

## Verständnis des Diagramms mit unterbrochener Achse

Nehmen wir einen Moment Zeit, um die Schlüsselkomponenten unseres Diagramms mit unterbrochener Achse zu verstehen:

1. **Zwei Teilplots**: Wir haben zwei separate Teilplots erstellt, die sich jeweils auf einen anderen Bereich von y-Werten konzentrieren.
2. **Ausgeblendete Achsenlinien**: Wir haben die verbindenden Achsenlinien zwischen den Teilplots ausgeblendet, um eine visuelle Trennung zu schaffen.
3. **Diagonale Unterbrechungslinien**: Wir haben diagonale Linien hinzugefügt, um anzuzeigen, dass die Achse unterbrochen ist.
4. **y-Achsengrenzen**: Wir haben für jeden Teilplot unterschiedliche y-Achsengrenzen festgelegt, um uns auf bestimmte Teile der Daten zu konzentrieren.
5. **Gitterlinien**: Wir haben Gitterlinien hinzugefügt, um die Lesbarkeit zu verbessern und es einfacher zu machen, Werte abzuschätzen.

Diese Technik ist besonders nützlich, wenn Sie in Ihren Daten Ausreißer haben, die sonst die Visualisierung der Mehrheit Ihrer Datenpunkte komprimieren würden. Durch das "Unterbrechen" der Achse können Sie sowohl die Ausreißer als auch die Hauptdatenverteilung deutlich in einem einzigen Diagramm anzeigen.

## Experimentieren mit dem Diagramm

Jetzt, da Sie verstehen, wie Sie ein Diagramm mit unterbrochener Achse erstellen, können Sie mit verschiedenen Konfigurationen experimentieren. Versuchen Sie, die y-Achsengrenzen zu ändern, weitere Merkmale zum Diagramm hinzuzufügen oder diese Technik auf Ihre eigenen Daten anzuwenden.

Beispielsweise können Sie den vorherigen Code ändern, um eine Legende hinzuzufügen, das Farbschema zu ändern oder die Markierungsstile anzupassen:

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes with different styles
ax1.plot(pts, 'o-', color='darkblue', label='Data Points', linewidth=2)
ax2.plot(pts, 'o-', color='darkblue', linewidth=2)

# Mark the outliers with a different color
outlier_indices = [3, 14]
ax1.plot(outlier_indices, pts[outlier_indices], 'ro', markersize=8, label='Outliers')

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

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers - Enhanced Visualization', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

# Add a legend to the top subplot
ax1.legend(loc='upper right')

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

Wenn Sie diesen erweiterten Code ausführen, sollten Sie eine verbesserte Visualisierung sehen, bei der die Ausreißer speziell markiert sind und eine Legende die Datenpunkte erklärt.

Herzlichen Glückwunsch! Sie haben erfolgreich ein Diagramm mit unterbrochener Achse in Python mit Matplotlib erstellt. Diese Technik wird Ihnen helfen, effektivere Visualisierungen zu erstellen, wenn Sie mit Daten umgehen, die Ausreißer enthalten.
