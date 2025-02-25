# Créer le premier graphique d'événements - orientation horizontale

Nous allons créer le premier graphique d'événements en orientation horizontale.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```
