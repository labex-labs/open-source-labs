# Erstellen einer Figur mit vier Teilplots

Wir werden eine Figur mit vier Teilplots erstellen, um die verschiedenen Aspekte der Ver光栅isierung zu veranschaulichen.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```