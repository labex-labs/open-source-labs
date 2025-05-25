# Definir a função do histograma empilhado

Definiremos uma função para criar um histograma empilhado. A função receberá os seguintes parâmetros:

- `ax`: os eixos para adicionar artistas
- `stacked_data`: um array com formato (M, N). A primeira dimensão será iterada para calcular histogramas linha a linha
- `sty_cycle`: um Cycler (ciclo) ou operável de dict, estilo a ser aplicado a cada conjunto
- `bottoms`: um array, padrão: 0, as posições iniciais das bases.
- `hist_func`: um callable (chamável), opcional. Deve ter a assinatura `bin_vals, bin_edges = f(data)`. Espera-se que `bin_edges` seja um elemento mais longo que `bin_vals`
- `labels`: uma lista de strings, opcional, o rótulo para cada conjunto. Se não for fornecido e os dados empilhados forem um array, o padrão será 'conjunto padrão {n}'. Se stacked_data for um mapeamento e labels for None, o padrão será as chaves. Se stacked_data for um mapeamento e labels for fornecido, apenas as colunas listadas serão plotadas.
- `plot_func`: um callable, opcional, função a ser chamada para desenhar o histograma. Deve ter a assinatura `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)`
- `plot_kwargs`: um dicionário, opcional, quaisquer argumentos de palavra-chave extras para passar para a função de plotagem. Isso será o mesmo para todas as chamadas para a função de plotagem e substituirá os valores em `sty_cycle`.

```python
def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    """
    Parâmetros
    ----------
    ax : axes.Axes
        Os eixos para adicionar artistas

    stacked_data : array or Mapping
        Um array com formato (M, N). A primeira dimensão será iterada para
        calcular histogramas linha a linha

    sty_cycle : Cycler ou operável de dict
        Estilo a ser aplicado a cada conjunto

    bottoms : array, padrão: 0
        As posições iniciais das bases.

    hist_func : callable, opcional
        Deve ter a assinatura `bin_vals, bin_edges = f(data)`.
        Espera-se que `bin_edges` seja um elemento mais longo que `bin_vals`

    labels : list of str, opcional
        O rótulo para cada conjunto.

        Se não for fornecido e os dados empilhados forem um array, o padrão será
        'conjunto padrão {n}'

        Se *stacked_data* for um mapeamento, e *labels* for None, o padrão será as
        chaves.

        Se *stacked_data* for um mapeamento e *labels* for fornecido, apenas as
        colunas listadas serão plotadas.

    plot_func : callable, opcional
        Função a ser chamada para desenhar o histograma deve ter a assinatura:

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : dict, opcional
        Quaisquer argumentos de palavra-chave extras para passar para a função de
        plotagem. Isso será o mesmo para todas as chamadas para a função de
        plotagem e substituirá os valores em *sty_cycle*.

    Retorna
    -------
    arts : dict
        Dicionário de artistas indexados em seus rótulos
    """
    # lidar com a função de binning padrão
    if hist_func is None:
        hist_func = np.histogram

    # lidar com a função de plotagem padrão
    if plot_func is None:
        plot_func = filled_hist

    # lidar com o padrão
    if plot_kwargs is None:
        plot_kwargs = {}

    try:
        l_keys = stacked_data.keys()
        label_data = True
        if labels is None:
            labels = l_keys

    except AttributeError:
        label_data = False
        if labels is None:
            labels = itertools.repeat(None)

    if label_data:
        loop_iter = enumerate((stacked_data[lab], lab, s) for lab, s in zip(labels, sty_cycle))
    else:
        loop_iter = enumerate(zip(stacked_data, labels, sty_cycle))

    arts = {}
    for j, (data, label, sty) in loop_iter:
        if label is None:
            label = f'dflt set {j}'
        label = sty.pop('label', label)
        vals, edges = hist_func(data)
        if bottoms is None:
            bottoms = np.zeros_like(vals)
        top = bottoms + vals
        sty.update(plot_kwargs)
        ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **sty)
        bottoms = top
        arts[label] = ret
    ax.legend(fontsize=10)
    return arts
```
