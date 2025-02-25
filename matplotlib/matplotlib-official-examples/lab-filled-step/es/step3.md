# Definir la función de histograma apilado

Definiremos una función para crear un histograma apilado. La función tomará los siguientes parámetros:

- `ax`: los ejes a los que se agregarán los artistas
- `stacked_data`: una matriz con forma (M, N). La primera dimensión se iterará para calcular los histogramas fila por fila
- `sty_cycle`: un Cycler o objeto operable de diccionarios, el estilo que se aplicará a cada conjunto
- `bottoms`: una matriz, valor predeterminado: 0, las posiciones iniciales de las bases
- `hist_func`: una función llamada, opcional. Debe tener la firma `bin_vals, bin_edges = f(data)`. Se espera que `bin_edges` sea una unidad más larga que `bin_vals`
- `labels`: una lista de cadenas, opcional, la etiqueta para cada conjunto. Si no se da y los datos apilados son una matriz, el valor predeterminado es 'conjunto predeterminado {n}'. Si `stacked_data` es un mapeo y `labels` es None, el valor predeterminado es las claves. Si `stacked_data` es un mapeo y se dan `labels`, entonces solo se graficarán las columnas listadas
- `plot_func`: una función llamada, opcional, función que se llamará para dibujar el histograma. Debe tener la firma `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)`
- `plot_kwargs`: un diccionario, opcional, cualquier argumento de palabras clave adicional que se transmitirá a la función de trazado. Esto será el mismo para todas las llamadas a la función de trazado y sobrescribirá los valores en `sty_cycle`.

```python
def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    """
    Parámetros
    ----------
    ax : axes.Axes
        Los ejes a los que se agregarán los artistas

    stacked_data : matriz o Mapeo
        Una matriz con forma (M, N).  La primera dimensión se iterará para
        calcular los histogramas fila por fila

    sty_cycle : Cycler o objeto operable de diccionarios
        Estilo que se aplicará a cada conjunto

    bottoms : matriz, valor predeterminado: 0
        Las posiciones iniciales de las bases.

    hist_func : callable, opcional
        Debe tener la firma `bin_vals, bin_edges = f(data)`.
        Se espera que `bin_edges` sea una unidad más larga que `bin_vals`

    labels : lista de str, opcional
        La etiqueta para cada conjunto.

        Si no se da y los datos apilados son una matriz, el valor predeterminado es 'conjunto predeterminado {n}'

        Si *stacked_data* es un mapeo, y *labels* es None, el valor predeterminado es las
        claves.

        Si *stacked_data* es un mapeo y *labels* se da, entonces solo se graficarán las
        columnas listadas.

    plot_func : callable, opcional
        Función que se llamará para dibujar el histograma debe tener la firma:

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : dict, opcional
        Cualquier argumento de palabras clave adicional que se transmitirá a la función de trazado.
        Esto será el mismo para todas las llamadas a la función de trazado y sobrescribirá los valores en *sty_cycle*.

    Devuelve
    -------
    arts : dict
        Diccionario de artistas con sus etiquetas como claves
    """
    # manejar la función de agrupamiento de intervalos predeterminada
    if hist_func is None:
        hist_func = np.histogram

    # manejar la función de trazado predeterminada
    if plot_func is None:
        plot_func = filled_hist

    # manejar el predeterminado
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
