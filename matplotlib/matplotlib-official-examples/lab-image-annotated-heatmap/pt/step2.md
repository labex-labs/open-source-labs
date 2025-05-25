# Usando o Estilo de Código da Função Auxiliar

Criaremos uma função que recebe os dados e os rótulos das linhas e colunas como entrada e permite argumentos que são usados para personalizar o gráfico. Desativaremos as bordas dos eixos circundantes e criaremos uma grade de linhas brancas para separar as células. Aqui, também queremos criar uma barra de cores e posicionar os rótulos acima do _heatmap_ em vez de abaixo dele. As anotações devem ter cores diferentes, dependendo de um limite para melhor contraste em relação à cor do pixel.

```python
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw=None, cbarlabel="", **kwargs):
    """
    Cria um heatmap a partir de um array numpy e duas listas de rótulos.

    Parâmetros
    ----------
    data
        Um array numpy 2D de forma (M, N).
    row_labels
        Uma lista ou array de comprimento M com os rótulos para as linhas.
    col_labels
        Uma lista ou array de comprimento N com os rótulos para as colunas.
    ax
        Uma instância `matplotlib.axes.Axes` para a qual o heatmap é plotado. Se não fornecido, use os eixos atuais ou crie um novo. Opcional.
    cbar_kw
        Um dicionário com argumentos para `matplotlib.Figure.colorbar`. Opcional.
    cbarlabel
        O rótulo para a barra de cores. Opcional.
    **kwargs
        Todos os outros argumentos são encaminhados para `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}", textcolors=("black", "white"), threshold=None, **textkw):
    """
    Uma função para anotar um heatmap.

    Parâmetros
    ----------
    im
        O AxesImage a ser rotulado.
    data
        Dados usados para anotar. Se None, os dados da imagem são usados. Opcional.
    valfmt
        O formato das anotações dentro do heatmap. Isso deve usar o método de formatação de string, por exemplo, "$ {x:.2f}", ou ser um `matplotlib.ticker.Formatter`. Opcional.
    textcolors
        Um par de cores. A primeira é usada para valores abaixo de um limite, a segunda para aqueles acima. Opcional.
    threshold
        Valor em unidades de dados de acordo com o qual as cores de textcolors são aplicadas. Se None (o padrão), usa o meio do mapa de cores como separação. Opcional.
    **kwargs
        Todos os outros argumentos são encaminhados para cada chamada para `text` usada para criar os rótulos de texto.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be overwritten by textkw.
    kw = dict(horizontalalignment="center", verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
```
