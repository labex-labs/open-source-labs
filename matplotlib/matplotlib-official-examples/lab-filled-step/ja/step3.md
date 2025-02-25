# 積み重ねヒストグラム関数を定義する

積み重ねヒストグラムを作成する関数を定義します。この関数は以下のパラメータを取ります。

- `ax`：アーティストを追加するAxes
- `stacked_data`：(M, N) の形状の配列。最初の次元を反復処理して、行方向にヒストグラムを計算します。
- `sty_cycle`：各セットに適用するスタイルを表すCyclerまたは辞書の操作可能なオブジェクト
- `bottoms`：配列、既定値: 0、下端の初期位置
- `hist_func`：コール可能オブジェクト（オプション）。署名 `bin_vals, bin_edges = f(data)` を持たなければなりません。`bin_edges` は `bin_vals` よりも1つ長いことが期待されます。
- `labels`：文字列のリスト（オプション）、各セットのラベル。指定されない場合、stacked_dataが配列の場合は 'default set {n}' が既定値となります。stacked_dataがマッピングで、labelsがNoneの場合はキーが既定値となります。stacked_dataがマッピングで、labelsが指定された場合は、列挙された列のみが描画されます。
- `plot_func`：コール可能オブジェクト（オプション）、ヒストグラムを描画するために呼び出す関数。署名 `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)` を持たなければなりません。
- `plot_kwargs`：辞書（オプション）、描画関数に渡す任意の追加のキーワード引数。これは、描画関数のすべての呼び出しに対して同じで、sty_cycle内の値を上書きします。

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
    # 既定のビニング関数を処理する
    if hist_func is None:
        hist_func = np.histogram

    # 既定の描画関数を処理する
    if plot_func is None:
        plot_func = filled_hist

    # 既定を処理する
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
