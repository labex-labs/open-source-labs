# Verwendung des Hilfsfunktions-Code-Stils

Wir werden eine Funktion erstellen, die die Daten sowie die Zeilen- und Spaltenbeschriftungen als Eingabe nimmt und Argumente zulässt, die zum Anpassen des Diagramms verwendet werden. Wir werden die umgebenden Achsenkanten deaktivieren und ein Gitter aus weißen Linien erstellen, um die Zellen voneinander zu trennen. Hier möchten wir auch eine Farbskala erstellen und die Beschriftungen über der Heatmap statt darunter positionieren. Die Anmerkungen sollen je nach Schwellenwert unterschiedliche Farben erhalten, um einen besseren Kontrast zu der Pixelfarbe zu erzielen.

```python
def heatmap(data, row_labels, col_labels, ax=None, cbar_kw=None, cbarlabel="", **kwargs):
    """
    Erstellt eine Heatmap aus einem numpy-Array und zwei Listen von Beschriftungen.

    Parameter
    ----------
    data
        Ein 2D numpy-Array der Größe (M, N).
    row_labels
        Eine Liste oder ein Array der Länge M mit den Beschriftungen für die Zeilen.
    col_labels
        Eine Liste oder ein Array der Länge N mit den Beschriftungen für die Spalten.
    ax
        Eine `matplotlib.axes.Axes`-Instanz, auf die die Heatmap geplottet wird. Wenn nicht angegeben, wird die aktuelle Achse verwendet oder eine neue erstellt. Optional.
    cbar_kw
        Ein Wörterbuch mit Argumenten für `matplotlib.Figure.colorbar`. Optional.
    cbarlabel
        Die Bezeichnung für die Farbskala. Optional.
    **kwargs
        Alle anderen Argumente werden an `imshow` weitergeleitet.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plotte die Heatmap
    im = ax.imshow(data, **kwargs)

    # Erstelle die Farbskala
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Zeige alle Striche und beschrifte sie mit den jeweiligen Listeinträgen.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Lasse die horizontale Achsenbeschriftung oben erscheinen.
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Drehe die Strichmarkenbeschriftungen und setze ihre Ausrichtung.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

    # Deaktiviere die Kanten und erstelle ein weißes Gitter.
    ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}", textcolors=("black", "white"), threshold=None, **textkw):
    """
    Eine Funktion, um eine Heatmap zu annotieren.

    Parameter
    ----------
    im
        Das AxesImage, das beschriftet werden soll.
    data
        Die Daten, die zur Annotation verwendet werden. Wenn None, werden die Daten des Bilds verwendet. Optional.
    valfmt
        Das Format der Anmerkungen innerhalb der Heatmap. Dies sollte entweder die String-Format-Methode verwenden, z.B. "$ {x:.2f}", oder ein `matplotlib.ticker.Formatter` sein. Optional.
    textcolors
        Ein Paar von Farben. Die erste wird für Werte unterhalb einer Schwelle verwendet, die zweite für die oberhalb. Optional.
    threshold
        Wert in Daten-Einheiten, gemäß dem die Farben aus textcolors angewendet werden. Wenn None (Standard), wird die Mitte der Farbskala als Trennung verwendet. Optional.
    **kwargs
        Alle anderen Argumente werden an jeden Aufruf von `text` weitergeleitet, der verwendet wird, um die Textbeschriftungen zu erstellen.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalisiere die Schwelle auf den Farbbereich des Bilds.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Setze die Standardausrichtung auf zentriert, aber gestatten es, durch textkw überschrieben zu werden.
    kw = dict(horizontalalignment="center", verticalalignment="center")
    kw.update(textkw)

    # Hole den Formatter, falls ein String übergeben wird
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Schleife über die Daten und erstelle für jedes "Pixel" ein `Text`.
    # Ändere die Farbe des Texts je nach Daten.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts
```
