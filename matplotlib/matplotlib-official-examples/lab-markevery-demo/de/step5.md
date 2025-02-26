# Erstellen von Polarkoordinaten-Graphen

Schließlich erstellen wir eine Reihe von Teilgraphen, um zu zeigen, wie `markevery` auf Polarkoordinaten-Graphen verhält. Wir stellen fest, dass das Verhalten ähnlich zu dem bei linearen Skalen ist.

```python
# create polar plots
r = np.linspace(0, 3.0, 200)
theta = 2 * np.pi * r

fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained',
                        subplot_kw={'projection': 'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(theta, r, 'o', ls='-', ms=4, markevery=markevery)
```
