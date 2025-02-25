# Création d'un graphique en barres au style xkcd

Dans cette étape, nous allons créer un graphique en barres au style xkcd. Le graphique est basé sur la bande dessinée "Les données jusqu'à présent" de XKCD.

```python
with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.bar([0, 1], [0, 100], 0.25)
    ax.spines[['top', 'right']].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['CONFIRMÉ PAR\nEXPÉRIENCE', 'RÉFUTÉ PAR\nEXPÉRIENCE'])
    ax.set_xlim([-0.5, 1.5])
    ax.set_yticks([])
    ax.set_ylim([0, 110])

    ax.set_title("PRÉTENTIONS DE POUVOIRS SURNATURELS")

    fig.text(
        0.5, 0.05,
        '"Les données jusqu'à présent" de xkcd par Randall Munroe',
        ha='center')

plt.show()
```
