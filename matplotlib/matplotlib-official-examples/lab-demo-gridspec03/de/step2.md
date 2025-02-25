# Teilplots mit `GridSpec` generieren

In diesem Schritt werden wir `GridSpec` verwenden, um Teilplots zu generieren. Wir werden eine Figur mit 2 Zeilen und 2 Spalten erstellen. Wir werden auch die `width_ratios` und `height_ratios` angeben, um die relativen Größen der Teilplots zu steuern.

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
