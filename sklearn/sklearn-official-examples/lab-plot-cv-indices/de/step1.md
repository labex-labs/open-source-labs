# Visualisiere die Daten

In diesem Schritt werden wir die Daten visualisieren, mit denen wir arbeiten werden. Die Daten bestehen aus 100 zufällig generierten Eingabedatenpunkten, 3 Klassen, die ungleichmäßig über die Datenpunkte verteilt sind, und 10 "Gruppen", die gleichmäßig über die Datenpunkte verteilt sind.

```python
# Generate the class/group data
n_points = 100
X = rng.randn(100, 10)

percentiles_classes = [0.1, 0.3, 0.6]
y = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentiles_classes)])

# Generate uneven groups
group_prior = rng.dirichlet([2] * 10)
groups = np.repeat(np.arange(10), rng.multinomial(100, group_prior))


def visualize_groups(classes, groups, name):
    # Visualize dataset groups
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
        yticklabels=["Data\ngroup", "Data\nclass"],
        xlabel="Sample index",
    )


visualize_groups(y, groups, "no groups")
```

# Visualisiere die Daten

In diesem Schritt visualisieren wir die Daten, mit denen wir arbeiten werden. Die Daten bestehen aus 100 zufällig generierten Eingabedatenpunkten, 3 Klassen, die ungleichmäßig über die Datenpunkte verteilt sind, und 10 "Gruppen", die gleichmäßig über die Datenpunkte verteilt sind.

```python
# Generiere die Klassendaten/Gruppendaten
n_points = 100
X = rng.randn(100, 10)

percentiles_classes = [0,1, 0,3, 0,6]
y = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentiles_classes)])

# Generiere ungleiche Gruppen
group_prior = rng.dirichlet([2] * 10)
groups = np.repeat(np.arange(10), rng.multinomial(100, group_prior))


def visualize_groups(classes, groups, name):
    # Visualisiere die Datensatzgruppen
    fig, ax = plt.subplots()
    ax.scatter(
        range(len(groups)),
        [0,5] * len(groups),
        c=groups,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.scatter(
        range(len(groups)),
        [3,5] * len(groups),
        c=classes,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.set(
        ylim=[-1, 5],
        yticks=[0,5, 3,5],
        yticklabels=["Data\ngroup", "Data\nclass"],
        xlabel="Sample index",
    )


visualize_groups(y, groups, "no groups")
```
