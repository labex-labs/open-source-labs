# Definiere die gestapelte Histogrammfunktion

Wir werden eine Funktion definieren, um ein gestapeltes Histogramm zu erstellen. Die Funktion nimmt die folgenden Parameter:

- `ax`: Die Achsen, denen Künstler hinzugefügt werden sollen
- `stacked_data`: Ein Array der Form (M, N). Die erste Dimension wird iteriert, um die Histogramme zeilenweise zu berechnen
- `sty_cycle`: Ein Cycler oder ein dict-fähiges Objekt, der Stil, der auf jede Menge angewendet werden soll
- `bottoms`: Ein Array, Standardwert: 0, die Anfangspositionen der Unterkanten
- `hist_func`: Ein aufrufbares Objekt, optional. Muss die Signatur `bin_vals, bin_edges = f(data)` haben. `bin_edges` sollte um eins länger als `bin_vals` sein
- `labels`: Eine Liste von Strings, optional, das Label für jede Menge. Wenn nicht angegeben und `stacked_data` ein Array ist, standardmäßig 'default set {n}'. Wenn `stacked_data` ein Mapping ist und `labels` None ist, standardmäßig die Schlüssel. Wenn `stacked_data` ein Mapping ist und `labels` angegeben ist, werden nur die aufgelisteten Spalten geplottet
- `plot_func`: Ein aufrufbares Objekt, optional, Funktion, die aufgerufen wird, um das Histogramm zu zeichnen. Muss die Signatur `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)` haben
- `plot_kwargs`: Ein Dictionary, optional, alle zusätzlichen Schlüsselwortargumente, die an die Plotfunktion weitergeleitet werden sollen. Dies wird für alle Aufrufe der Plotfunktion gleich sein und wird die Werte in `sty_cycle` überschreiben

```python
def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    """
    Parameter
    ----------
    ax : axes.Axes
        Die Achsen, denen Künstler hinzugefügt werden sollen

    stacked_data : array oder Mapping
        Ein Array der Form (M, N).  Die erste Dimension wird iteriert, um
        die Histogramme zeilenweise zu berechnen

    sty_cycle : Cycler oder operable of dict
        Stil, der auf jede Menge angewendet werden soll

    bottoms : array, default: 0
        Die Anfangspositionen der Unterkanten.

    hist_func : callable, optional
        Muss die Signatur `bin_vals, bin_edges = f(data)` haben.
        `bin_edges` sollte um eins länger als `bin_vals` sein

    labels : liste von str, optional
        Das Label für jede Menge.

        Wenn nicht angegeben und `stacked_data` ein Array ist, standardmäßig 'default set {n}'

        Wenn *stacked_data* ein Mapping ist, und *labels* ist None, standardmäßig die
        Schlüssel.

        Wenn *stacked_data* ein Mapping ist und *labels* angegeben ist, werden nur die
        aufgelisteten Spalten geplottet.

    plot_func : callable, optional
        Funktion, die aufgerufen wird, um das Histogramm zu zeichnen, muss die Signatur haben:

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : dict, optional
        Alle zusätzlichen Schlüsselwortargumente, die an die Plotfunktion weitergeleitet werden sollen.
        Dies wird für alle Aufrufe der Plotfunktion gleich sein und wird
        die Werte in *sty_cycle* überschreiben.

    Rückgabe
    -------
    arts : dict
        Dictionary von Künstlern, die nach ihren Labels indiziert sind
    """
    # Gehe mit der Standard-Binning-Funktion um
    if hist_func is None:
        hist_func = np.histogram

    # Gehe mit der Standard-Plotfunktion um
    if plot_func is None:
        plot_func = filled_hist

    # Gehe mit dem Standard um
    if plot_kwargs is None:
        plot_kwargs = {}

    versuche:
        l_keys = stacked_data.keys()
        label_data = True
        if labels is None:
            labels = l_keys

    außer AttributeError:
        label_data = False
        if labels is None:
            labels = itertools.repeat(None)

    if label_data:
        loop_iter = enumerate((stacked_data[lab], lab, s) für lab, s in zip(labels, sty_cycle))
    sonst:
        loop_iter = enumerate(zip(stacked_data, labels, sty_cycle))

    arts = {}
    für j, (data, label, sty) in loop_iter:
        wenn label ist None:
            label = f'dflt set {j}'
        label = sty.pop('label', label)
        vals, edges = hist_func(data)
        wenn bottoms ist None:
            bottoms = np.zeros_like(vals)
        top = bottoms + vals
        sty.update(plot_kwargs)
        ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **sty)
        bottoms = top
        arts[label] = ret
    ax.legend(fontsize=10)
    return arts
```
