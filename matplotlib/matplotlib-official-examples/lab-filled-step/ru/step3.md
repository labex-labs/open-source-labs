# Определяем функцию для накопленной гистограммы

Мы определим функцию для создания накопленной гистограммы. Функция будет принимать следующие параметры:

- `ax`: оси, на которые будут добавлены элементы графика
- `stacked_data`: массив формы (M, N). Первая размерность будет итерироваться для вычисления гистограмм по строкам
- `sty_cycle`: Cycler или итерируемый объект словарей, стиль, который будет применяться к каждой группе
- `bottoms`: массив, по умолчанию: 0, начальные позиции нижних частей столбцов
- `hist_func`: вызываемая функция, необязательная. Должен иметь сигнатуру `bin_vals, bin_edges = f(data)`. `bin_edges` ожидается на один элемент длиннее, чем `bin_vals`
- `labels`: список строк, необязательный, метка для каждой группы. Если не задано и `stacked_data` - это массив, по умолчанию используется 'default set {n}'. Если `stacked_data` - это словарь и `labels` равен None, по умолчанию используются ключи. Если `stacked_data` - это словарь и `labels` задан, то будут нарисованы только перечисленные столбцы
- `plot_func`: вызываемая функция, необязательная, функция, которая будет вызываться для рисования гистограммы. Должен иметь сигнатуру `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)`
- `plot_kwargs`: словарь, необязательный, любые дополнительные именованные аргументы, которые будут переданы в функцию рисования. Это будет одинаково для всех вызовов функции рисования и будет переопределять значения в `sty_cycle`

```python
def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    """
    Parameters
    ----------
    ax : axes.Axes
        The axes to add artists too

    stacked_data : array or Mapping
        A (M, N) shaped array.  The first dimension will be iterated over to
        compute histograms row-wise

    sty_cycle : Cycler or operable of dict
        Style to apply to each set

    bottoms : array, default: 0
        The initial positions of the bottoms.

    hist_func : callable, optional
        Must have signature `bin_vals, bin_edges = f(data)`.
        `bin_edges` expected to be one longer than `bin_vals`

    labels : list of str, optional
        The label for each set.

        If not given and stacked data is an array defaults to 'default set {n}'

        If *stacked_data* is a mapping, and *labels* is None, default to the
        keys.

        If *stacked_data* is a mapping and *labels* is given then only the
        columns listed will be plotted.

    plot_func : callable, optional
        Function to call to draw the histogram must have signature:

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : dict, optional
        Any extra keyword arguments to pass through to the plotting function.
        This will be the same for all calls to the plotting function and will
        override the values in *sty_cycle*.

    Returns
    -------
    arts : dict
        Dictionary of artists keyed on their labels
    """
    # deal with default binning function
    if hist_func is None:
        hist_func = np.histogram

    # deal with default plotting function
    if plot_func is None:
        plot_func = filled_hist

    # deal with default
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
