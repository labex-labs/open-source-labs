# Erstellen von Teilbildern ohne Constrained Layout

Wir erstellen eine Figur mit 2x2 Teilbildern, ohne das _constrained layout_ zu verwenden. Dies führt zu überlappenden Beschriftungen auf den Achsen.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```
