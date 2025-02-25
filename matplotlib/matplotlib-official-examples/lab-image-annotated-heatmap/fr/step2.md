# Utilisation du style de code de la fonction d'aide

Nous allons créer une fonction qui prend les données et les étiquettes de ligne et de colonne en entrée et accepte des arguments utilisés pour personnaliser le tracé. Nous allons désactiver les bords des axes environnants et créer une grille de lignes blanches pour séparer les cellules. Ici, nous voulons également créer une barre de couleur et positionner les étiquettes au-dessus de la carte thermique plutôt qu'au-dessous. Les annotations devront avoir des couleurs différentes selon un seuil pour un meilleur contraste avec la couleur des pixels.

```python
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw=None, cbarlabel="", **kwargs):
    """
    Crée une carte thermique à partir d'un tableau numpy et de deux listes d'étiquettes.

    Paramètres
    ----------
    data
        Un tableau numpy 2D de forme (M, N).
    row_labels
        Une liste ou un tableau de longueur M avec les étiquettes pour les lignes.
    col_labels
        Une liste ou un tableau de longueur N avec les étiquettes pour les colonnes.
    ax
        Une instance de `matplotlib.axes.Axes` sur laquelle la carte thermique est tracée. Si non fourni, utilise l'axe courant ou en crée un nouveau. Facultatif.
    cbar_kw
        Un dictionnaire avec des arguments pour `matplotlib.Figure.colorbar`. Facultatif.
    cbarlabel
        L'étiquette pour la barre de couleur. Facultatif.
    **kwargs
        Tous les autres arguments sont transmis à `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Trace la carte thermique
    im = ax.imshow(data, **kwargs)

    # Crée la barre de couleur
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Affiche toutes les graduations et les étiquette avec les entrées respectives de la liste.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Fait apparaître les étiquettes des axes horizontaux en haut.
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Fait tourner les étiquettes des graduations et définit leur alignement.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

    # Désactive les bords et crée une grille blanche.
    ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}", textcolors=("black", "white"), threshold=None, **textkw):
    """
    Une fonction pour annoter une carte thermique.

    Paramètres
    ----------
    im
        L'AxesImage à étiqueter.
    data
        Données utilisées pour l'étiquetage. Si None, les données de l'image sont utilisées. Facultatif.
    valfmt
        Le format des annotations à l'intérieur de la carte thermique. Cela devrait utiliser soit la méthode de formatage de chaîne, par exemple, "$ {x:.2f}", soit être un `matplotlib.ticker.Formatter`. Facultatif.
    textcolors
        Une paire de couleurs. La première est utilisée pour les valeurs inférieures à un seuil, la seconde pour celles au-dessus. Facultatif.
    threshold
        Valeur en unités de données selon laquelle les couleurs de textcolors sont appliquées. Si None (la valeur par défaut), utilise le milieu de la carte de couleur comme séparation. Facultatif.
    **kwargs
        Tous les autres arguments sont transmis à chaque appel à `text` utilisé pour créer les étiquettes de texte.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalise le seuil à la plage de couleur de l'image.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Définit l'alignement par défaut sur le centre, mais autorise qu'il soit remplacé par textkw.
    kw = dict(horizontalalignment="center", verticalalignment="center")
    kw.update(textkw)

    # Obtient le formateur au cas où une chaîne est fournie
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Parcoure les données et crée un `Text` pour chaque "pixel".
    # Change la couleur du texte selon les données.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
```
