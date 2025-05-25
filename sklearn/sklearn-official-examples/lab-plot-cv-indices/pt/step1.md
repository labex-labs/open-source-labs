# Visualizar os Dados

Nesta etapa, visualizaremos os dados com os quais trabalharemos. Os dados consistem em 100 pontos de dados de entrada gerados aleatoriamente, 3 classes divididas de forma desigual entre os pontos de dados e 10 "grupos" divididos igualmente entre os pontos de dados.

```python
# Gerar os dados de classe/grupo
n_pontos = 100
X = rng.randn(100, 10)

percentis_classes = [0.1, 0.3, 0.6]
y = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentis_classes)])

# Gerar grupos desiguais
prior_grupo = rng.dirichlet([2] * 10)
grupos = np.repeat(np.arange(10), rng.multinomial(100, prior_grupo))


def visualizar_grupos(classes, grupos, nome):
    # Visualizar os grupos de dados
    fig, ax = plt.subplots()
    ax.scatter(
        range(len(grupos)),
        [0.5] * len(grupos),
        c=grupos,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.scatter(
        range(len(grupos)),
        [3.5] * len(grupos),
        c=classes,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.set(
        ylim=[-1, 5],
        yticks=[0.5, 3.5],
        yticklabels=["Grupo de\ndados", "Classe\nde dados"],
        xlabel="Índice da amostra",
    )


visualizar_grupos(y, grupos, "sem grupos")
```
