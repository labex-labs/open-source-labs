# Créer une figure avec des sous-graphiques

Maintenant, nous allons créer une figure avec quatre sous-graphiques, un pour chaque ensemble de données. Nous allons également définir les limites x et y pour être les mêmes pour tous les sous-graphiques.

```python
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.08})
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
```
