# Festlegen der Plotgrenzen und -beschriftungen

Wir werden die Plotgrenzen und -beschriftungen so einstellen, dass sie der gewünschten Ausgabe entsprechen.

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```
