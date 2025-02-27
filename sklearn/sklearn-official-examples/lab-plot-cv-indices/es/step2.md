# Visualizar los índices de validación cruzada

En este paso, definiremos una función para visualizar el comportamiento de cada objeto de validación cruzada. Realizaremos 4 divisiones del data. En cada división, visualizaremos los índices elegidos para el conjunto de entrenamiento (en azul) y el conjunto de prueba (en rojo).

```python
def plot_cv_indices(cv, X, y, group, ax, n_splits, lw=10):
    """Create a sample plot for indices of a cross-validation object."""

    # Generate the training/testing visualizations for each CV split
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # Fill in indices with the training/test groups
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # Visualize the results
        ax.scatter(
            range(len(indices)),
            [ii + 0.5] * len(indices),
            c=indices,
            marker="_",
            lw=lw,
            cmap=cmap_cv,
            vmin=-0.2,
            vmax=1.2,
        )

    # Plot the data classes and groups at the end
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # Formatting
    yticklabels = list(range(n_splits)) + ["class", "group"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="Índice de muestra",
        ylabel="Iteración de validación cruzada",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```

# Visualizar los índices de validación cruzada

En este paso, definiremos una función para visualizar el comportamiento de cada objeto de validación cruzada. Realizaremos 4 divisiones del data. En cada división, visualizaremos los índices elegidos para el conjunto de entrenamiento (en azul) y el conjunto de prueba (en rojo).

```python
def graficar_indices_cv(cv, X, y, group, ax, n_splits, lw=10):
    """Crear una gráfica de muestra para los índices de un objeto de validación cruzada."""

    # Generar las visualizaciones de entrenamiento/prueba para cada división de validación cruzada
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # Llenar los índices con los grupos de entrenamiento/prueba
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # Visualizar los resultados
        ax.scatter(
            range(len(indices)),
            [ii + 0.5] * len(indices),
            c=indices,
            marker="_",
            lw=lw,
            cmap=cmap_cv,
            vmin=-0.2,
            vmax=1.2,
        )

    # Graficar las clases y grupos de datos al final
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # Formateo
    yticklabels = list(range(n_splits)) + ["clase", "grupo"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="Índice de muestra",
        ylabel="Iteración de validación cruzada",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```
