# Fonction d'aide

Avant de présenter chacun des noyaux disponibles pour les processus gaussiens, nous définirons une fonction d'aide permettant de tracer des échantillons tirés du processus gaussien.

```python
def plot_gpr_samples(gpr_model, n_samples, ax):
    """Trace des échantillons tirés du modèle de processus gaussien.

    Si le modèle de processus gaussien n'est pas entraîné, les échantillons tirés sont
    tirés de la distribution a priori. Sinon, les échantillons sont tirés de
    la distribution a posteriori. Sachez qu'un échantillon ici correspond à une
    fonction.

    Paramètres
    ----------
    gpr_model : `GaussianProcessRegressor`
        Un modèle :class:`~sklearn.gaussian_process.GaussianProcessRegressor`.
    n_samples : int
        Le nombre d'échantillons à tirer de la distribution du processus gaussien.
    ax : axe matplotlib
        L'axe matplotlib où tracer les échantillons.
    """
    x = np.linspace(0, 5, 100)
    X = x.reshape(-1, 1)

    y_mean, y_std = gpr_model.predict(X, return_std=True)
    y_samples = gpr_model.sample_y(X, n_samples)

    for idx, single_prior in enumerate(y_samples.T):
        ax.plot(
            x,
            single_prior,
            linestyle="--",
            alpha=0.7,
            label=f"Fonction échantillonnée #{idx + 1}",
        )
    ax.plot(x, y_mean, color="black", label="Moyenne")
    ax.fill_between(
        x,
        y_mean - y_std,
        y_mean + y_std,
        alpha=0.1,
        color="black",
        label=r"$\pm$ 1 écart-type.",
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim([-3, 3])
```
