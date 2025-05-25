# Plotar Distribuições

Finalmente, criamos uma função para plotar cada distribuição e chamamos a função para cada distribuição na lista. A função mostrará dois gráficos para cada escalonador/transformador/normalizador. O gráfico da esquerda mostra um gráfico de dispersão do conjunto de dados completo, e o gráfico da direita exclui os valores extremos, considerando apenas 99% do conjunto de dados, excluindo outliers marginais. Além disso, as distribuições marginais para cada recurso serão mostradas nas laterais do gráfico de dispersão.

```python
# Plotar distribuições
def plot_distribution(axes, X, y, hist_nbins=50, title="", x0_label="", x1_label=""):
    ax, hist_X1, hist_X0 = axes

    ax.set_title(title)
    ax.set_xlabel(x0_label)
    ax.set_ylabel(x1_label)

    # O gráfico de dispersão
    colors = cm.plasma_r(y)
    ax.scatter(X[:, 0], X[:, 1], alpha=0.5, marker="o", s=5, lw=0, c=colors)

    # Removendo as linhas superior e direita para estética
    # Criar um layout de eixos agradável
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines["left"].set_position(("outward", 10))
    ax.spines["bottom"].set_position(("outward", 10))

    # Histograma para o eixo X1 (recurso 5)
    hist_X1.set_ylim(ax.get_ylim())
    hist_X1.hist(
        X[:, 1], bins=hist_nbins, orientation="horizontal", color="grey", ec="grey"
    )
    hist_X1.axis("off")

    # Histograma para o eixo X0 (recurso 0)
    hist_X0.set_xlim(ax.get_xlim())
    hist_X0.hist(
        X[:, 0], bins=hist_nbins, orientation="vertical", color="grey", ec="grey"
    )
    hist_X0.axis("off")


# escalonar a saída entre 0 e 1 para a barra de cores
y = minmax_scale(y_full)

# plasma não existe no matplotlib < 1.5
cmap = getattr(cm, "plasma_r", cm.hot_r)

def create_axes(title, figsize=(16, 6)):
    fig = plt.figure(figsize=figsize)
    fig.suptitle(title)

    # definir o eixo para o primeiro gráfico
    # ... (código restante)
```
