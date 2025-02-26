# Erstellen von vergrößerten Graphen

Wir erstellen eine weitere Reihe von Teilgraphen, um diesmal zu zeigen, wie `markevery` auf vergrößerten Graphen verhält. Wir stellen fest, dass die ganzzahlbasierte Subsampling Punkte aus den zugrunde liegenden Daten auswählt und unabhängig von der Ansicht ist, während die fließkommazahlbasierte Subsampling mit der Achsen-Diagonalen zusammenhängt und den angezeigten Datensatz ändert.

```python
# create zoomed plots
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
