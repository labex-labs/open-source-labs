# Erstellen von Teilplots

Wir werden nun ein 2x2-Gitter von Teilplots mit der `subplots`-Funktion erstellen. Dies wird uns vier Plots geben, um das Sparsamkeitmuster des Arrays zu visualisieren.

```python
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
```
