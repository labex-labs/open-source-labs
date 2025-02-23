# Ausrichte die y-Beschriftungen manuell

Der vierte Schritt besteht darin, die y-Beschriftungen manuell mit der Methode `~.Axis.set_label_coords` des y-Achsenobjekts auszurichten.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

labex = -0.3  # Achsenkoordinaten

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labex, 0.5)

plt.show()
```
