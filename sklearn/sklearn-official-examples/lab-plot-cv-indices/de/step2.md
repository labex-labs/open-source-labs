# Visualisiere die Indizes der Kreuzvalidierung

In diesem Schritt definieren wir eine Funktion, um das Verhalten jedes Kreuzvalidierungsobjekts zu visualisieren. Wir werden 4 Aufteilungen der Daten vornehmen. Bei jeder Aufteilung visualisieren wir die Indizes, die für den Trainingssatz (blau) und den Testsatz (rot) ausgewählt wurden.

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
        xlabel="Sample index",
        ylabel="CV iteration",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```

# Visualisiere die Indizes der Kreuzvalidierung

In diesem Schritt definieren wir eine Funktion, um das Verhalten jedes Kreuzvalidierungsobjekts zu visualisieren. Wir werden 4 Aufteilungen der Daten vornehmen. Bei jeder Aufteilung visualisieren wir die Indizes, die für den Trainingssatz (blau) und den Testsatz (rot) ausgewählt wurden.

```python
def plot_cv_indices(cv, X, y, group, ax, n_splits, lw=10):
    """Erstelle ein Beispielplot für die Indizes eines Kreuzvalidierungsobjekts."""

    # Generiere die Visualisierungen für die Trainings- und Testdaten für jede Kreuzvalidierungsaufteilung
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # Fülle die Indizes mit den Trainings- und Testgruppen
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # Visualisiere die Ergebnisse
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

    # Plotte die Datenklassen und -gruppen am Ende
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # Formatierung
    yticklabels = list(range(n_splits)) + ["class", "group"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="Sample index",
        ylabel="CV iteration",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```
