# Définissez la fonction d'histogramme empilé

Nous allons définir une fonction pour créer un histogramme empilé. La fonction prendra les paramètres suivants :

- `ax` : les axes sur lesquels ajouter des artistes
- `stacked_data` : un tableau de forme (M, N). La première dimension sera itérée pour calculer les histogrammes ligne par ligne
- `sty_cycle` : un Cycler ou un opérable de dict, le style à appliquer à chaque ensemble
- `bottoms` : un tableau, valeur par défaut : 0, les positions initiales des fonds
- `hist_func` : une fonction appelable, optionnelle. Doit avoir la signature `bin_vals, bin_edges = f(data)`. `bin_edges` est supposé être d'une longueur supérieure de 1 à `bin_vals`
- `labels` : une liste de chaînes de caractères, optionnelle, l'étiquette pour chaque ensemble. Si non fourni et que les données empilées sont un tableau, la valeur par défaut est 'ensemble par défaut {n}'. Si stacked_data est un mapping et labels est None, la valeur par défaut est les clés. Si stacked_data est un mapping et labels est donné, alors seulement les colonnes listées seront tracées.
- `plot_func` : une fonction appelable, optionnelle, fonction à appeler pour tracer l'histogramme. Doit avoir la signature `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)`
- `plot_kwargs` : un dictionnaire, optionnel, tous les autres arguments clés à passer à la fonction de tracé. Ceci sera le même pour tous les appels à la fonction de tracé et remplacera les valeurs dans `sty_cycle`.

```python
def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    """
    Paramètres
    ----------
    ax : axes.Axes
        Les axes sur lesquels ajouter des artistes

    stacked_data : array ou Mapping
        Un tableau de forme (M, N).  La première dimension sera itérée pour
        calculer les histogrammes ligne par ligne

    sty_cycle : Cycler ou opérable de dict
        Style à appliquer à chaque ensemble

    bottoms : array, valeur par défaut: 0
        Les positions initiales des fonds.

    hist_func : callable, optionnel
        Doit avoir la signature `bin_vals, bin_edges = f(data)`.
        `bin_edges` est supposé être d'une longueur supérieure de 1 à `bin_vals`

    labels : list of str, optionnel
        L'étiquette pour chaque ensemble.

        Si non fourni et que les données empilées sont un tableau, la valeur par défaut est 'ensemble par défaut {n}'

        Si *stacked_data* est un mapping, et *labels* est None, la valeur par défaut est les clés.

        Si *stacked_data* est un mapping et *labels* est donné, alors seulement les
        colonnes listées seront tracées.

    plot_func : callable, optionnel
        Fonction à appeler pour tracer l'histogramme doit avoir la signature :

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : dict, optionnel
        Tous les autres arguments clés à passer à la fonction de tracé.
        Ceci sera le même pour tous les appels à la fonction de tracé et remplacera les valeurs dans *sty_cycle*.

    Retours
    -------
    arts : dict
        Dictionnaire d'artistes indexé sur leurs étiquettes
    """
    # gérer la fonction de découpage par défaut
    if hist_func is None:
        hist_func = np.histogram

    # gérer la fonction de tracé par défaut
    if plot_func is None:
        plot_func = filled_hist

    # gérer la valeur par défaut
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
