# Abstand um und zwischen Teilplots steuern

In diesem Schritt werden wir `GridSpec` verwenden, um den Abstand um und zwischen Teilplots zu steuern. Wir werden eine Figur mit 2 GridSpecs erstellen, wobei jeder 3 Zeilen und 3 Spalten hat. Wir werden die Parameter `left`, `right`, `bottom`, `top`, `wspace` und `hspace` angeben, um den Abstand zu steuern.

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```
