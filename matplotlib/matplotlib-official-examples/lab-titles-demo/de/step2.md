# Linke und rechte Titelpositionierung

Matplotlib ermöglicht es Ihnen, den Titel auf der linken oder rechten Seite des Diagramms zu positionieren, indem Sie den Parameter `loc` verwenden. In diesem Schritt lernen Sie, wie Sie Titel links und rechts in Ihren Diagrammen ausrichten können.

## Erstellen eines Diagramms mit einem linksbündigen Titel

Erstellen wir ein Diagramm, bei dem der Titel auf der linken Seite positioniert ist. Geben Sie in einer neuen Zelle den folgenden Code ein:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Left-Aligned Title', loc='left')  # Position the title at the left
plt.show()
```

![left-aligned-title](../assets/screenshot-20250306-9pLPZz36@2x.png)

Führen Sie die Zelle aus. Beachten Sie, wie der Titel jetzt linksbündig am Diagrammrand und nicht mehr zentriert erscheint.

Der Parameter `loc` in der Funktion `title()` bestimmt die horizontale Position des Titels. Indem Sie `loc='left'` festlegen, sagen Sie Matplotlib, den Titel auf der linken Seite des Diagramms zu positionieren.

## Erstellen eines Diagramms mit einem rechtsbündigen Titel

Jetzt erstellen wir ein weiteres Diagramm, bei dem der Titel auf der rechten Seite positioniert ist. Geben Sie in einer neuen Zelle den folgenden Code ein:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Right-Aligned Title', loc='right')  # Position the title at the right
plt.show()
```

![right-aligned-title](../assets/screenshot-20250306-PpNxbjp2@2x.png)

Führen Sie die Zelle aus. Der Titel sollte jetzt rechtsbündig am Diagrammrand erscheinen.

## Vergleich verschiedener Titelpositionen

Erstellen wir eine Abfolge von drei Diagrammen, um die verschiedenen Titelpositionen (zentriert, links und rechts) zu vergleichen. Geben Sie in einer neuen Zelle den folgenden Code ein:

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Center-aligned title (default)
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Center Title')

# Plot 2: Left-aligned title
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Left Title', loc='left')

# Plot 3: Right-aligned title
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Right Title', loc='right')

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

![three-title-positions](../assets/screenshot-20250306-EzNR2plC@2x.png)

Führen Sie die Zelle aus, um alle drei Titelpositionen nebeneinander zu sehen. Dieser visuelle Vergleich hilft Ihnen zu verstehen, wie der Parameter `loc` die Titelpositionierung beeinflusst.

Beachten Sie, dass wir bei der Arbeit mit Teil-Diagrammen (Subplots) die Methode `set_title()` auf den einzelnen Achsenobjekten anstelle der globalen Funktion `plt.title()` verwenden.
