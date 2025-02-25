# Erstellen eines Diagramms mit vier Teilbildern

Wir werden ein Diagramm mit vier Teilbildern erstellen, um die verschiedenen Aspekte der Ver光栅isierung zu veranschaulichen.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
