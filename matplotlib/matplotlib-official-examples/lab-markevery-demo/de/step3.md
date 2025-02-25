# Erstellen von Graphen mit logarithmischen Skalen

Wir wiederholen den vorherigen Schritt, aber diesmal mit logarithmischen Skalen. Wir stellen fest, dass die logarithmische Skala eine visuelle Asymmetrie in der Markierungsdistanz bei der ganzzahlbasierten Subsampling verursacht, während die bruchbasierten Subsampling gleichmäßige Verteilungen erzeugt.

```python
# create plots with logarithmic scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, fälle):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
