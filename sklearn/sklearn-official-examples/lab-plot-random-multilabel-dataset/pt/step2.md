# Definir a Função de Plotagem

Em seguida, definimos uma função `plot_2d` que plota o conjunto de dados multirótulo gerado aleatoriamente. Ela recebe três argumentos: `n_labels`, `n_classes` e `length`.

```python
def plot_2d(ax, n_labels=1, n_classes=3, length=50):
    X, Y, p_c, p_w_c = make_ml_clf(
        n_samples=150,
        n_features=2,
        n_classes=n_classes,
        n_labels=n_labels,
        length=length,
        allow_unlabeled=False,
        return_distributions=True,
        random_state=RANDOM_SEED,
    )

    ax.scatter(
        X[:, 0], X[:, 1], color=COLORS.take((Y * [1, 2, 4]).sum(axis=1)), marker="."
    )
    ax.scatter(
        p_w_c[0] * length,
        p_w_c[1] * length,
        marker="*",
        linewidth=0.5,
        edgecolor="black",
        s=20 + 1500 * p_c**2,
        color=COLORS.take([1, 2, 4]),
    )
    ax.set_xlabel("Contagem da Característica 0")
    return p_c, p_w_c
```

Esta função gera o conjunto de dados utilizando a função `make_multilabel_classification` com os parâmetros especificados. Em seguida, plota o conjunto de dados usando a função `scatter` da biblioteca Matplotlib. A função retorna as probabilidades de classe e as probabilidades de características.
