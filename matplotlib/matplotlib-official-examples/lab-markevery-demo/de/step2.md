# Erstellen von Graphen mit linearen Skalen

Als nächstes erstellen wir eine Reihe von Teilgraphen, um zu zeigen, wie `markevery` mit linearen Skalen umgeht. Wir iterieren durch die Liste `fälle` und plotten jeden Fall in einem separaten Teilgraphen. Wir verwenden den Parameter `markevery`, um anzugeben, welche Datenpunkte markiert werden sollen.

```python
# create plots with linear scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, fälle):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
