# Création d'un graphique au style xkcd

Dans cette étape, nous allons créer un graphique au style xkcd qui montre la relation entre le temps et la santé globale. Le graphique est basé sur la bande dessinée "Propriété d'un fourneau" de XKCD.

```python
with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)

    ax.annotate(
        'LE JOUR OÙ J\'AI COMPRIS QUE JE POUVAIS\nCUISINER DU BACON\nQUAND JE VEUX',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

    ax.plot(data)

    ax.set_xlabel('time')
    ax.set_ylabel('ma santé globale')
    fig.text(
        0.5, 0.05,
        '"Propriété d'un fourneau" de xkcd par Randall Munroe',
        ha='center')

plt.show()
```
