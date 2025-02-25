# Définissez la fonction d'histogramme

Nous allons définir une fonction pour tracer un histogramme sous forme d'un patch en escalier. La fonction prendra les paramètres suivants :

- `ax` : les Axes sur lesquels tracer
- `edges` : un tableau de longueur n+1 donnant les bords gauche de chaque boîte et le bord droit de la dernière boîte
- `values` : un tableau de longueur n des comptes ou des valeurs des boîtes
- `bottoms` : un nombre ou un tableau, optionnel, un tableau de longueur n du bas des barres. Si None, on utilise zéro.
- `orientation` : une chaîne de caractères, optionnelle, l'orientation de l'histogramme. 'v' (par défaut) a les barres croissant dans la direction y positive.

```python
def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    """
    Trace un histogramme sous forme d'un patch en escalier.

    Paramètres
    ----------
    ax : Axes
        Les axes sur lesquels tracer

    edges : tableau
        Un tableau de longueur n+1 donnant les bords gauche de chaque boîte et le
        bord droit de la dernière boîte.

    values : tableau
        Un tableau de longueur n des comptes ou des valeurs des boîtes

    bottoms : nombre ou tableau, optionnel
        Un tableau de longueur n du bas des barres.  Si None, on utilise zéro.

    orientation : {'v', 'h'}
       Orientation de l'histogramme.  'v' (par défaut) a
       les barres croissant dans la direction y positive.

    **kwargs
        Les autres arguments clés sont transmis à `.fill_between`.

    Retours
    -------
    ret : PolyCollection
        Artiste ajouté aux Axes
    """
    if orientation not in 'hv':
        raise ValueError(f"orientation doit être dans {{'h', 'v'}} et non {orientation}")

    kwargs.setdefault('step', 'post')
    kwargs.setdefault('alpha', 0.7)
    edges = np.asarray(edges)
    values = np.asarray(values)
    if len(edges) - 1!= len(values):
        raise ValueError(f'Doit fournir un bord de boîte de plus que de valeur et non : {len(edges)=} {len(values)=}')

    if bottoms is None:
        bottoms = 0
    bottoms = np.broadcast_to(bottoms, values.shape)

    values = np.append(values, values[-1])
    bottoms = np.append(bottoms, bottoms[-1])
    if orientation == 'h':
        return ax.fill_betweenx(edges, values, bottoms, **kwargs)
    elif orientation == 'v':
        return ax.fill_between(edges, values, bottoms, **kwargs)
    else:
        raise AssertionError("vous ne devriez jamais être ici")
```
