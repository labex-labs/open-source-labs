# Visualiser les données

Dans cette étape, nous allons visualiser les données avec lesquelles nous allons travailler. Les données sont composées de 100 points de données d'entrée générés aléatoirement, de 3 classes réparties de manière inégale parmi les points de données et de 10 "groupes" répartis régulièrement parmi les points de données.

```python
# Générer les données de classe/groupe
n_points = 100
X = rng.randn(100, 10)

percentiles_classes = [0.1, 0.3, 0.6]
y = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentiles_classes)])

# Générer des groupes inégaux
group_prior = rng.dirichlet([2] * 10)
groups = np.repeat(np.arange(10), rng.multinomial(100, group_prior))


def visualize_groups(classes, groups, name):
    # Visualiser les groupes du jeu de données
    fig, ax = plt.subplots()
    ax.scatter(
        range(len(groups)),
        [0.5] * len(groups),
        c=groups,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.scatter(
        range(len(groups)),
        [3.5] * len(groups),
        c=classes,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.set(
        ylim=[-1, 5],
        yticks=[0.5, 3.5],
        yticklabels=["Données\ngroupe", "Données\nclasse"],
        xlabel="Index d'échantillonnage"
    )


visualize_groups(y, groups, "sans groupes")
```
