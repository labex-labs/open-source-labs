# Figur und Teilplots erstellen

Wir müssen eine Figur und Teilplots erstellen, um die Daten anzuzeigen. In diesem Lab werden wir zwei nebeneinander liegende Teilplots erstellen.

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
