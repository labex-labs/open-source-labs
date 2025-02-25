# Funktion definieren

Jetzt werden wir eine Funktion namens `survey` definieren, die die `results` und `category_names` entgegennimmt und eine horizontale gestapelte Balkendiagrammvisualisierung erstellt.

```python
def survey(results, category_names):
    """
    Parameter
    ----------
    results : dict
        Ein Mapping von Fragenbezeichnungen zu einer Liste von Antworten pro Kategorie.
        Es wird angenommen, dass alle Listen die gleiche Anzahl von Einträgen enthalten und dass
        sie der Länge von *category_names* entspricht.
    category_names : Liste von str
        Die Kategoriebezeichnungen.
    """
    # Konvertiere die Ergebnisse und Kategorien zu numpy-Arrays
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # Berechne kumulative Summen der Daten für die horizontale Stapelung
    data_cum = data.cumsum(axis=1)

    # Definiere Kategorie-Farben
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # Erstelle das Diagramm und setze Achseigenschaften
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # Erstelle die gestapelten Balken und füge Balkenbeschriftungen hinzu
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # Füge Legende hinzu
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```
