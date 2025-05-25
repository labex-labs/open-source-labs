# Função auxiliar

Antes de apresentar cada kernel individual disponível para processos gaussianos, definiremos uma função auxiliar que nos permitirá plotar amostras extraídas do processo gaussiano.

```python
def plot_gpr_samples(gpr_model, n_samples, ax):
    """Plotar amostras extraídas do modelo de processo gaussiano.

    Se o modelo de processo gaussiano não estiver treinado, as amostras extraídas serão
    extraídas da distribuição a priori. Caso contrário, as amostras serão extraídas da
    distribuição a posteriori. Note que uma amostra aqui corresponde a uma
    função.

    Parâmetros
    ----------
    gpr_model : `GaussianProcessRegressor`
        Um modelo :class:`~sklearn.gaussian_process.GaussianProcessRegressor`.
    n_samples : int
        O número de amostras a extrair da distribuição do processo gaussiano.
    ax : matplotlib axis
        O eixo matplotlib onde plotar as amostras.
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
            label=f"Função amostrada #{idx + 1}",
        )
    ax.plot(x, y_mean, color="black", label="Média")
    ax.fill_between(
        x,
        y_mean - y_std,
        y_mean + y_std,
        alpha=0.1,
        color="black",
        label=r"$\pm$ 1 desvio padrão",
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim([-3, 3])
```
