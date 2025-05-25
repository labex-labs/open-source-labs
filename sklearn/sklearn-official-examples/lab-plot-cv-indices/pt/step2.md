# Visualizar Índices de Validação Cruzada

Nesta etapa, definiremos uma função para visualizar o comportamento de cada objeto de validação cruzada. Realizaremos 4 divisões dos dados. Em cada divisão, visualizaremos os índices escolhidos para o conjunto de treinamento (em azul) e o conjunto de teste (em vermelho).

```python
def plot_cv_indices(cv, X, y, group, ax, n_splits, lw=10):
    """Criar um gráfico de amostra para índices de um objeto de validação cruzada."""

    # Gerar as visualizações de treinamento/teste para cada divisão de validação cruzada
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # Preencher os índices com os grupos de treinamento/teste
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # Visualizar os resultados
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

    # Plotar as classes e grupos de dados no final
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # Formatação
    yticklabels = list(range(n_splits)) + ["classe", "grupo"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="Índice da amostra",
        ylabel="Iteração de validação cruzada",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```
