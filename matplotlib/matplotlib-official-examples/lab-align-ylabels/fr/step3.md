# Aligner automatiquement les étiquettes sur l'axe des ordonnées

La troisième étape consiste à aligner automatiquement les étiquettes sur l'axe des ordonnées en utilisant la méthode `.Figure.align_ylabels`.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
fig.align_ylabels(axs[:, 1])
plt.show()
```
