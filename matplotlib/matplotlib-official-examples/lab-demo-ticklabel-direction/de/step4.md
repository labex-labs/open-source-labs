# Skalenbeschriftungen, die nach außen zeigen

In diesem Schritt werden wir einen Teilplot erstellen, bei dem die Skalenbeschriftungen nach außen zeigen.

```python
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.2)

ax = setup_axes(fig, 131)
for axis in ax.axis.values():
    axis.major_ticks.set_tick_out(True)
```
