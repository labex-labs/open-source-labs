# Erstellen von Teilbildern mit Constrained Layout

Wir erstellen die gleichen 2x2 Teilbilder, aber diesmal verwenden wir das _constrained layout_. Dies passt die Teilbilder automatisch an, um Überlappungen zwischen Achsenobjekten und Beschriftungen zu vermeiden.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```
