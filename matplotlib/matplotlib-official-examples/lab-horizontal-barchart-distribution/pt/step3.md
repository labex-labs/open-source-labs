# Definir Função

Agora, definiremos uma função chamada `survey` que recebe os `results` e `category_names` e cria uma visualização de gráfico de barras empilhadas horizontais.

```python
def survey(results, category_names):
    """
    Parâmetros
    ----------
    results : dict
        Um mapeamento de rótulos de perguntas para uma lista de respostas por categoria.
        Assume-se que todas as listas contêm o mesmo número de entradas e que
        corresponde ao comprimento de *category_names*.
    category_names : list of str
        Os rótulos das categorias.
    """
    # Converter os resultados e categorias para arrays numpy
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # Calcular somas cumulativas de dados para empilhamento horizontal
    data_cum = data.cumsum(axis=1)

    # Definir cores das categorias
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # Criar o gráfico e definir as propriedades dos eixos
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # Criar as barras empilhadas e adicionar rótulos às barras
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # Adicionar legenda
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```
