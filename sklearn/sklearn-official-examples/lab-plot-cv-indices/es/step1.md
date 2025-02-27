# Visualizar los datos

En este paso, visualizaremos los datos con los que trabajaremos. Los datos constan de 100 puntos de datos de entrada generados aleatoriamente, 3 clases divididas de manera desigual entre los puntos de datos y 10 "grupos" divididos equitativamente entre los puntos de datos.

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

# Visualizar los datos

En este paso, visualizaremos los datos con los que trabajaremos. Los datos constan de 100 puntos de datos de entrada generados aleatoriamente, 3 clases divididas de manera desigual entre los puntos de datos y 10 "grupos" divididos equitativamente entre los puntos de datos.

```python
# Generar los datos de clase/grupo
n_points = 100
X = rng.randn(100, 10)

percentiles_classes = [0.1, 0.3, 0.6]
y = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentiles_classes)])

# Generar grupos desiguales
group_prior = rng.dirichlet([2] * 10)
groups = np.repeat(np.arange(10), rng.multinomial(100, group_prior))


def visualizar_grupos(classes, groups, name):
    # Visualizar los grupos del conjunto de datos
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
        yticklabels=["Datos\ngrupo", "Datos\nclase"],
        xlabel="Índice de muestra",
    )


visualizar_grupos(y, groups, "sin grupos")
```
