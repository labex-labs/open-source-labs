# Eine Abbildung mit vier Teilplots erstellen

Wir werden eine Abbildung mit vier Teilplots erstellen, um verschiedene Aspekte der Rasterisierung zu veranschaulichen.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```