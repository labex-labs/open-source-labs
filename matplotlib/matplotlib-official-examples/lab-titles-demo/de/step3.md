# Benutzerdefinierte vertikale Titelpositionierung

Manchmal möchten Sie möglicherweise die vertikale Position Ihres Titels anpassen. In diesem Schritt lernen Sie, wie Sie die vertikale (y-Achse) Position der Diagrammtitel manuell steuern können.

## Grundlegendes zur Y-Position in Titeln

Die vertikale Position eines Titels kann mithilfe des Parameters `y` in der Funktion `title()` angepasst werden. Der Parameter `y` akzeptiert Werte in normalisierten Koordinaten, wobei:

- `y = 1.0` (Standard) platziert den Titel oben am Diagramm
- `y > 1.0` platziert den Titel über dem oberen Rand des Diagramms
- `y < 1.0` platziert den Titel unter dem oberen Rand des Diagramms, näher am Diagramminhalt

## Erstellen eines Diagramms mit benutzerdefinierter Y-Position des Titels

Erstellen wir ein Diagramm, bei dem der Titel höher als standardmäßig positioniert ist. Geben Sie in einer neuen Zelle den folgenden Code ein:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Higher Title Position', y=1.1)  # Position the title higher
plt.show()
```

Führen Sie die Zelle aus. Beachten Sie, wie der Titel jetzt im Vergleich zur Standardposition etwas höher über dem Diagramm erscheint.

Jetzt erstellen wir ein Diagramm, bei dem der Titel tiefer als standardmäßig positioniert ist:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Lower Title Position', y=0.9)  # Position the title lower
plt.show()
```

Führen Sie die Zelle aus. Der Titel sollte jetzt näher am Diagramminhalt erscheinen.

## Vergleich verschiedener Y-Positionen

Erstellen wir mehrere Diagramme nebeneinander, um verschiedene vertikale Titelpositionen zu vergleichen:

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Default Y-position
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Default Position (y=1.0)')

# Plot 2: Higher Y-position
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Higher Position', y=1.15)

# Plot 3: Lower Y-position
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Lower Position', y=0.85)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

Führen Sie die Zelle aus, um alle drei vertikalen Positionen nebeneinander zu sehen. Dieser Vergleich hilft Ihnen zu verstehen, wie der Parameter `y` die vertikale Position des Titels beeinflusst.

## Kombination von horizontaler und vertikaler Positionierung

Sie können den Parameter `loc` (für die horizontale Ausrichtung) mit dem Parameter `y` (für die vertikale Position) kombinieren, um den Titel genau dort zu platzieren, wo Sie ihn haben möchten:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Custom Positioned Title', loc='right', y=1.1)  # Right-aligned and higher
plt.show()
```

Führen Sie die Zelle aus. Der Titel sollte jetzt rechtsbündig am Diagrammrand erscheinen und höher als standardmäßig positioniert sein.
