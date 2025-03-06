# Fortgeschrittene Titelpositionierung mit Teil-Diagrammen (Subplots)

In diesem Schritt lernen Sie fortgeschrittene Techniken zur Titelpositionierung, wenn Sie mit Teil-Diagramm-Layouts (Subplot-Layouts) und Achsenobjekten arbeiten. Sie erfahren auch, wie Sie die Funktion `suptitle()` verwenden können, um einem Diagramm mit mehreren Teil-Diagrammen einen Gesamt-Titel hinzuzufügen.

## Erstellen eines Diagramms mit Teil-Diagrammen und individuellen Titeln

Erstellen wir ein 2x2-Raster von Teil-Diagrammen, wobei jedes seinen eigenen, unterschiedlich positionierten Titel hat:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data and set titles with different positions for each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# Top-left subplot: Default centered title
axes[0].set_title('Default (Centered)')

# Top-right subplot: Left-aligned title
axes[1].set_title('Left-Aligned', loc='left')

# Bottom-left subplot: Right-aligned title
axes[2].set_title('Right-Aligned', loc='right')

# Bottom-right subplot: Custom positioned title
axes[3].set_title('Custom Position', y=0.85, loc='center')

# Add spacing between subplots
plt.tight_layout()
plt.show()
```

Führen Sie die Zelle aus. Sie sollten vier Teil-Diagramme sehen, jedes mit einem unterschiedlich positionierten Titel.

## Hinzufügen eines Diagramm-Titels mit `suptitle()`

Wenn Sie mit mehreren Teil-Diagrammen arbeiten, möchten Sie möglicherweise einen Gesamt-Titel für das gesamte Diagramm hinzufügen. Dies kann mit der Funktion `suptitle()` erreicht werden:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# Add an overall title to the figure
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Führen Sie die Zelle aus. Sie sollten vier Teil-Diagramme sehen, jedes mit seinem eigenen Titel, und einen Gesamt-Titel für das Diagramm oben.

## Kombination von Achsen-Titeln und Diagramm-Titeln

Sie können individuelle Teil-Diagramm-Titel mit einem Gesamt-Diagramm-Titel kombinieren:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot with different title positions
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# Add an overall title to the figure
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Führen Sie die Zelle aus. Sie sollten ein Diagramm mit vier Teil-Diagrammen sehen, jedes mit einem unterschiedlich positionierten Titel, und einen Gesamt-Titel oben am Diagramm.

Die Funktion `suptitle()` ist nützlich, um einen Haupt-Titel hinzuzufügen, der das gesamte Diagramm beschreibt, während einzelne Aufrufe von `set_title()` auf Achsenobjekten spezifischere Titel für jedes Teil-Diagramm hinzufügen.
