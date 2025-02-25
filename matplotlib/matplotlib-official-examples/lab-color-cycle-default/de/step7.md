# Anpassen der y-Achsenmarkierungen

Wir passen die y-Achsenmarkierungen für die am linkesten liegenden Teilplots an.

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
